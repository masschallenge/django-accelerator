import swapper

from datetime import datetime
from django.db.models import (
    OuterRef,
    Q,
    Subquery
)
from django.urls import reverse
from django.utils import timezone
from pytz import utc
from accelerator.models import (
    CoreProfile,
    UserRole,
)
from accelerator.utils import UserAlert
from accelerator_abstract.models import (
    ACTIVE_PANEL_STATUS,
    ACTIVE_PROGRAM_STATUS,
    BIO_MAX_LENGTH,
    CAPTURE_AVAILABILITY_DISABLED,
    ENDED_PROGRAM_STATUS,
    HIDDEN_PROGRAM_STATUS,
    UPCOMING_PROGRAM_STATUS,
)
from accelerator_abstract.models.base_judging_round import (
    ONLINE_JUDGING_ROUND_TYPE,
)

SHORT_BIO_MAX_LENGTH = 140
CONFIRMED_FOR_MESSAGE = "<h4>%s, you are confirmed for %s:</h4>"
EXPECTING_TO_SEE_YOU_MESSAGE = ("<p>&nbsp;</p><h4>We are expecting "
                                "to see you at %s.</h4>")
SINGLE_PANEL_MESSAGE = "this upcoming judging panel"
MULTIPLE_PANELS_MESSAGE = "these upcoming judging panels"
OFFICE_HOUR_HOLDER_ROLES = [UserRole.MENTOR, UserRole.AIR]
OFFICE_HOURS_HOLDER = Q(
    program_role__user_role__name__in=OFFICE_HOUR_HOLDER_ROLES)
ACTIVE_PROGRAM = Q(program_role__program__program_status='active')

PLEASE_INFORM_US_MESSAGE = ("<p>&nbsp;</p><p><b>PLEASE INFORM US IMMEDIATELY "
                            'AT <a href="mailto:%s">%s</a>'
                            "IF YOU ARE NO LONGER ABLE TO MAKE %s. "
                            "THANKS!</b></p>")
ACTIVE_IN_PERSON_JUDGING_MESSAGE = (
    'You are assigned to an active judging panel, please'
    '&nbsp;<b><a class="btn btn-primary btn-large" href="%s">'
    'go to your judging portal to review applications</a></b>'
    '<p>&nbsp;</p>'
)

ONGOING_ONLINE_JUDGING_NOTIFICATION = (
    'You are assigned to an active online judging round, please'
    '<p>&nbsp;</p><b><a class="btn btn-primary btn-large" href="%s">'
    'go to your judging portal to review applications</a></b>'
    '<p>&nbsp;</p>'
)

UPDATE_JUDGE_COMMITMENTS_NOTIFICATION = (
    'There are upcoming judging opportunities for you to revew. '
    '<b><a class="btn btn-primary btn-large" href="%s"> '
    'Update your judging commitments</a></b>'
    '<p>&nbsp;</p>'
)


class ExpertProfile(CoreProfile):
    user_type = 'expert'
    default_page = "expert_homepage"

    class Meta:
        db_table = 'accelerator_expertprofile'
        permissions = (
            ('change_password', 'Can change users passwords directly'),
        )
        swappable = swapper.swappable_setting(
            CoreProfile.Meta.app_label, "ExpertProfile")

    def judge_round_commitments(self):
        return self.user.judgeroundcommitment_set.all()

    @property
    def long_bio(self):
        return self._trimmed_bio(max_chars=BIO_MAX_LENGTH)

    @property
    def short_bio(self):
        return self._trimmed_bio(max_chars=SHORT_BIO_MAX_LENGTH)

    @property
    def mentor_profile_url(self):
        if self.is_mentor():
            return reverse('mentor_view', args=(self.user.id,))

    def _trimmed_bio(self, max_chars):
        bio = self.bio or ''
        if len(bio) > max_chars:
            bio = bio[:max_chars].rsplit(' ', 1)[0]
            bio = '%s...' % bio
        return bio

    def user_id(self):
        return self.user.id

    def first_name(self):
        return self.user.first_name

    def last_name(self):
        return self.user.last_name

    def email(self):
        return self.user.email

    def mentoring_specialty_names(self):
        return [
            str(specialty) for specialty in self.mentoring_specialties.all()]

    def additional_industry_names(self):
        return [
            industry.name for industry in self.additional_industries.all()]

    def functional_expertise_names(self):
        return [
            expertise.name for expertise in self.functional_expertise.all()]

    @property
    def active_round(self):
        return self.active_judging_rounds().first()

    def active_judging_rounds(self):
        JudgingRound = swapper.load_model('accelerator', 'JudgingRound')
        judge_grants = self.user.programrolegrant_set.filter(
            program_role__user_role__name=UserRole.JUDGE)
        program_ids = judge_grants.values_list('program_role__program_id')
        rounds = JudgingRound.objects.filter(
            is_active=True,
            program_id__in=program_ids)
        return rounds

    def has_invited_judging_rounds(self):
        # True iff judge has desired state for upcoming
        # judging rounds, for which they have no commitment object
        # note that commitement object can indicate "decline to commit"
        JudgingRound = swapper.load_model('accelerator', 'JudgingRound')
        return JudgingRound.objects.filter(
            start_date_time__gt=utc.localize(datetime.now()),
            desired_judge_label__in=self.user.userlabel_set.all()).exclude(
            judgeroundcommitment__judge=self.user).exists()

    def get_commitment(self, judging_round):
        if judging_round:
            return self.user.judgeroundcommitment_set.filter(
                judging_round=judging_round).first()
        else:
            return None

    def get_stats(self,
                  round_active=True,
                  judging_round=None):
        active_online_rounds = self.active_judging_rounds().filter(
            round_type=ONLINE_JUDGING_ROUND_TYPE)

        if not judging_round and (
                round_active and
                not active_online_rounds.exists()
        ):
            return {}

        assignment_counts = self.get_assignment_counts(
            round_active=round_active,
            judging_round=judging_round)
        stats = {
            'C': self.get_capacity(judging_round),
            'A': assignment_counts[0],
            'Q': min(
                assignment_counts[0], self.get_current_quota(judging_round)),
            'deadline': self.get_deadline(judging_round),
            'S': assignment_counts[1],
            'P': self.get_all_panel_assignments()
        }
        stats['due_now'] = max((stats['Q'] - stats['S']), 0)
        stats['additional_due'] = max(
            (max(stats['C'], stats['A']) - stats['S']) - stats['due_now'], 0)
        return stats

    def get_assignment_counts(self, round_active=True,
                              judging_round=None):
        """return the count of all applications and completed applications
        """
        user = self.user
        app_count = completed_count = 0
        panel_assignments = self.get_all_panel_assignments(
            round_active=round_active,
            judging_round=judging_round)
        for assignment in panel_assignments:
            assignment_completed = assignment.assignment_status == 'COMPLETE'
            panel = assignment.panel
            applications = panel.applications.all()
            forms = panel.get_feedback_forms_for_user(user)
            for application in applications:
                app_count += 1
                if assignment_completed:
                    form = forms.get(str(application.pk), None)
                    if form and form.feedback_status != 'INCOMPLETE':
                        completed_count += 1
        return app_count, completed_count

    def get_all_panel_assignments(self,
                                  round_active=True,
                                  future_only=False,
                                  judging_round=None):
        jpa_filter = self._create_jpa_filter(round_active,
                                             judging_round)
        jpas = self.user.judgepanelassignment_set.filter(
            **jpa_filter).order_by('panel__panel_time__start_date_time')
        if future_only:
            now = utc.localize(datetime.today())
            jpas = jpas.filter(panel__panel_time__start_date_time__gt=now)
        return jpas

    def get_active_assignments(self):
        jpas = self.get_all_panel_assignments(round_active=True)
        active_jpas = jpas.filter(panel__status=ACTIVE_PANEL_STATUS)
        return active_jpas

    def get_capacity(self, judging_round):
        """return the committed capacity of this judge for this active round
        """
        capacity = 0
        commitment = self.get_commitment(judging_round)
        try:
            capacity = commitment.capacity or 0
        except AttributeError:
            pass
        finally:
            return capacity

    def get_current_quota(self, judging_round):
        current_quota = 0
        commitment = self.get_commitment(judging_round)
        try:
            current_quota = commitment.current_quota or 0
        except AttributeError:
            pass
        finally:
            return current_quota

    def get_deadline(self, judging_round):
        if judging_round and judging_round.end_date_time:
            return judging_round.end_date_time
        else:
            return "N/A"

    def latest_active_program_location(self):
        prg = self._latest_confirmed_non_future_program_role_grant()
        if not prg:
            return None
        return prg.program_role.program.program_family.name

    def latest_active_program_year(self):
        prg = self._latest_confirmed_non_future_program_role_grant()
        if not prg:
            return None
        return str(prg.program_role.program.start_date.year)

    def confirmed_mentor_program_families(self):
        """
        Given that the Mentor Directory should not be empty,
        When all programs in a program family have ended
        We want to be able to show the mentors in the ended program
        But when a program is active, we shouldn't show the confirmed
        mentors of the ended program.
        SubQueries were leveraged for optimisation to reduce
        the number of queries.
        """
        prg = self._confirmed_non_future_program_role_grant()
        program_ids = self._latest_program_id_foreach_program_family()
        return list(prg.filter(
            program_role__program__pk__in=program_ids
        ).values_list(
            'program_role__program__program_family__name',
            flat=True).distinct())

    def _latest_program_id_foreach_program_family(self):
        ProgramFamily = swapper.load_model('accelerator', 'ProgramFamily')
        latest_program_subquery = self._program_family__program_subquery()
        return list(ProgramFamily.objects.annotate(
            latest_program=Subquery(latest_program_subquery)
        ).values_list("latest_program", flat=True))

    def _program_family__program_subquery(self):
        ProgramFamily = swapper.load_model('accelerator', 'ProgramFamily')
        return ProgramFamily.objects.filter(
            program_family=OuterRef('pk'),
            program_status__in=[ACTIVE_PROGRAM_STATUS, ENDED_PROGRAM_STATUS]
        ).order_by("-created_at").values('pk')[:1]

    def _latest_confirmed_non_future_program_role_grant(self):
        prg = self._confirmed_non_future_program_role_grant()
        return prg.order_by('-created_at').first()

    def _confirmed_non_future_program_role_grant(self):
        return self.user.programrolegrant_set.filter(
            program_role__user_role__name=UserRole.MENTOR).exclude(
            program_role__program__program_status__in=[
                HIDDEN_PROGRAM_STATUS,
                UPCOMING_PROGRAM_STATUS]
        ).prefetch_related(
            'program_role__program',
            'program_role__program__program_family'
        )

    def is_confirmed_mentor(self):
        return self.user.programrolegrant_set.filter(
            program_role__user_role__name=UserRole.MENTOR).exists()

    @classmethod
    def mentors(cls, program):
        role_name = UserRole.MENTOR
        return ExpertProfile.objects.filter(
            user__programrolegrant__program_role__program=program,
            user__programrolegrant__program_role__user_role__name=role_name)

    def is_judge(self, program=None, state=None):
        """Only experts may be judges."""
        """If program is specified, is the expert a judge in that program."""
        """Otherwise, is the expert a judge in any program."""
        role_dict = {'desired': [UserRole.DESIRED_JUDGE],
                     'confirmed': [UserRole.JUDGE]}
        roles = role_dict.get(state, [UserRole.DESIRED_JUDGE, UserRole.JUDGE])
        if program:
            return self.user.programrolegrant_set.filter(
                program_role__program__exact=program,
                program_role__user_role__name__in=roles).exists()
        else:
            return self.user.programrolegrant_set.filter(
                program_role__user_role__name__in=roles).exists()

    def get_active_alerts(self, page=None):
        """Return any active alerts for the user, that are relevant for
        the current 'page' of the application
        """
        alerts = []
        panels_url = reverse('panel_listing', urlconf="mc_judge.urls")

        if self.has_invited_judging_rounds():
            alerts.append(self._invited_judge_alert())

        active_rounds = self.active_judging_rounds()
        if self.is_judge(state="confirmed") and active_rounds.exists():
            alert = UserAlert()
            alert.alert_type = 'judge-portal-access'
            alert.alert_style = 'success'
            alert.message = ACTIVE_IN_PERSON_JUDGING_MESSAGE % panels_url

            alerts.append(alert)

        if self.is_judge() and self.get_active_assignments().exists():
            alert = UserAlert()
            alert.alert_type = 'judge-panel-active'
            alert.alert_style = 'warning'

            alert.message = (ONGOING_ONLINE_JUDGING_NOTIFICATION %
                             panels_url)
        return alerts

    def _invited_judge_alert(self):
        manage_url = reverse('manage_commitments')
        alert = UserAlert()
        alert.alert_type = 'judge-invite'
        alert.alert_style = 'success'
        alert.message = UPDATE_JUDGE_COMMITMENTS_NOTIFICATION % manage_url
        return alert

    def _create_jpa_filter(self, round_active, judging_round):
        # It would be better to somehow move this to JudgePanelAssignment or
        # a JudgePanelAssignmentManager object such that it can still
        # be accessed through self.judgepanelassignment_set, but I'm
        # not sure the best way to do that.
        filter = {
            'judge': self.user,
            'scenario__is_active': True
        }
        if judging_round:
            filter['scenario__judging_round'] = judging_round
            return filter
        if round_active:
            filter['scenario__judging_round__is_active__exact'] = True
        active_rounds = self.active_judging_rounds()
        if active_rounds.exists():
            filter['scenario__judging_round__in'] = active_rounds
        return filter

    def office_hour_programs(self):
        # returns a list of all active program ids associated with an expert
        # having open office hours
        has_available_office_hours = self.user.mentor_officehours.filter(
            finalist__isnull=True,
            start_date_time__gte=timezone.now()
        ).exists()
        if has_available_office_hours:
            return list(_get_office_hour_holder_active_programs(self.user))
        return []


def _recruiting_judges():
    capacity = Q(capture_capacity=True)
    availability = ~Q(capture_availability=CAPTURE_AVAILABILITY_DISABLED)
    return swapper.load_model('accelerator', 'JudgingRound').objects.filter(
        capacity | availability).exists()


def _get_office_hour_holder_active_programs(user):
    Clearance = swapper.load_model('accelerator', 'Clearance')
    clearances = Clearance.objects.clearances_for_user(user).filter(
        program_family__programs__program_status=ACTIVE_PROGRAM_STATUS
    )
    active_program_ids = set()
    active_program_ids.update(list(clearances.values_list(
        'program_family__programs__id', flat=True
    ).distinct()))
    active_program_ids.update(list(user.programrolegrant_set.filter(
        OFFICE_HOURS_HOLDER & ACTIVE_PROGRAM
    ).values_list('program_role__program__id', flat=True).distinct()))
    return active_program_ids
