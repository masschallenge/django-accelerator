import swapper
from pytz import utc
from datetime import (
    datetime,
    timedelta,
)
from django.db.models import (
    OuterRef,
    Q,
    Subquery,
)
from django.urls import reverse
from django.utils import timezone
from polymorphic.models import PolymorphicModel

from accelerator.models import UserRole
from accelerator_abstract.models import (
    ACTIVE_PROGRAM_STATUS,
    BIO_MAX_LENGTH,
    CLEARANCE_LEVEL_ORDER,
    CLEARANCE_LEVEL_STAFF,
    ENDED_PROGRAM_STATUS,
    HIDDEN_PROGRAM_STATUS,
    UPCOMING_PROGRAM_STATUS,
)
from accelerator_abstract.models.base_core_profile import BaseCoreProfile
from accelerator_abstract.models.base_judging_round import (
    ONLINE_JUDGING_ROUND_TYPE,
)
from accelerator_abstract.models.base_user_utils import is_employee

SHORT_BIO_MAX_LENGTH = 140
OFFICE_HOUR_HOLDER_ROLES = [UserRole.MENTOR, UserRole.AIR]
OFFICE_HOURS_HOLDER = Q(
    program_role__user_role__name__in=OFFICE_HOUR_HOLDER_ROLES)
ACTIVE_PROGRAM = Q(
    program_role__program__program_status=ACTIVE_PROGRAM_STATUS)


class CoreProfile(BaseCoreProfile, PolymorphicModel):
    class Meta(BaseCoreProfile.Meta):
        pass

    def first_name(self):
        return self.user.first_name

    def last_name(self):
        return self.user.last_name

    def startup_name(self):
        return self.user.startup_name()

    def email(self):
        return self.user.email

    def program(self):
        return self.user.program()

    def startup_industry(self):
        return self.user.startup_industry()

    def startup_status_names(self):
        return self.user.startup_status_names()

    def location(self):
        return self.user.location()

    def year(self):
        return self.user.year()

    def type(self):
        return self.user.type()

    def team_member_id(self):
        return self.user.team_member_id()

    def user_title(self):
        return self.user.user_title()

    def finalist_user_roles(self):
        return self.user.finalist_user_roles()

    def is_team_member(self):
        return self.user.is_team_member()

    def top_level_startup_industry(self):
        return self.user.top_level_startup_industry()

    def has_a_finalist_role(self):
        return self.user.has_a_finalist_role()

    def is_active(self):
        return self.user.is_active

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

    @property
    def active_round(self):
        return self.active_judging_rounds().first()

    def is_confirmed_mentor(self):
        return self.user.programrolegrant_set.filter(
            program_role__user_role__name=UserRole.MENTOR).exists()

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

    def functional_expertise_names(self):
        return [
            expertise.name for expertise in self.functional_expertise.all()]

    def mentoring_specialty_names(self):
        return [
            str(specialty) for specialty in self.mentoring_specialties.all()]

    def additional_industry_names(self):
        return [
            industry.name for industry in self.additional_industries.all()]

    def office_hour_programs(self):
        # returns a list of all active program ids associated with an expert
        # having open office hours
        has_available_office_hours = self.user.mentor_officehours.filter(
            finalist__isnull=True,
            start_date_time__gte=timezone.now()).exists()
        if has_available_office_hours:
            return list(_get_office_hour_holder_active_programs(self.user))
        return []

    def roles(self):
        user_roles = [UserRole.MENTOR, UserRole.FINALIST, UserRole.ALUM]
        roles_list = []
        if is_employee(self.user):
            roles_list.append(UserRole.STAFF)
        roles_list += list(self.user.programrolegrant_set.filter(
            program_role__user_role__name__in=user_roles).values_list(
            'program_role__user_role__name', flat=True).distinct())
        return roles_list

    def program_participation(self):
        participation_roles = [UserRole.MENTOR, UserRole.FINALIST]
        return list(self.user.programrolegrant_set.filter(
            Q(program_role__user_role__name__in=participation_roles)
            & ACTIVE_PROGRAM).values_list(
            'program_role__program__name', flat=True).distinct())

    def is_staff_in_active_program(self):
        Clearance = swapper.load_model('accelerator', 'Clearance')
        filter_kwargs = {
            'user': self.user,
            'order__lte': CLEARANCE_LEVEL_ORDER.get(CLEARANCE_LEVEL_STAFF),
            'program_family__programs__program_status': ACTIVE_PROGRAM_STATUS
        }
        return Clearance.objects.filter(**filter_kwargs).exists()

    def is_mentor_in_active_program(self):
        return self.user.programrolegrant_set.filter(
            program_role__user_role__name=UserRole.MENTOR,
            program_role__program__program_status=ACTIVE_PROGRAM_STATUS
        ).exists()

    def is_mentor_in_upcoming_program(self):
        return self.user.programrolegrant_set.filter(
            program_role__user_role__name=UserRole.MENTOR,
            program_role__program__program_status=UPCOMING_PROGRAM_STATUS
        ).exists()

    def was_mentor_in_last_12_months(self):
        year_ago = timezone.now() - timedelta(days=365)
        return self.user.programrolegrant_set.filter(
            program_role__user_role__name=UserRole.MENTOR,
            program_role__program__program_status=ENDED_PROGRAM_STATUS,
            program_role__program__end_date__gte=year_ago).exists()

    def _trimmed_bio(self, max_chars):
        bio = self.bio or ''
        if len(bio) > max_chars:
            bio = bio[:max_chars].rsplit(' ', 1)[0]
            bio = '%s...' % bio
        return bio

    def _confirmed_non_future_program_role_grant(self):
        return self.user.programrolegrant_set.filter(
            program_role__user_role__name=UserRole.MENTOR).exclude(
            program_role__program__program_status__in=[
                HIDDEN_PROGRAM_STATUS,
                UPCOMING_PROGRAM_STATUS]
        ).prefetch_related(
            'program_role__program',
            'program_role__program__program_family')

    def _latest_program_id_foreach_program_family(self):
        ProgramFamily = swapper.load_model('accelerator', 'ProgramFamily')
        latest_program_subquery = self._program_family__program_subquery()
        return list(ProgramFamily.objects.annotate(
            latest_program=Subquery(latest_program_subquery)
        ).values_list("latest_program", flat=True))

    def _latest_confirmed_non_future_program_role_grant(self):
        prg = self._confirmed_non_future_program_role_grant()
        return prg.order_by('-created_at').first()

    def _program_family__program_subquery(self):
        Program = swapper.load_model('accelerator', 'Program')
        return Program.objects.filter(
            program_family=OuterRef('pk'),
            program_status__in=[ACTIVE_PROGRAM_STATUS, ENDED_PROGRAM_STATUS]
        ).order_by("-created_at").values('pk')[:1]

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

    def active_judging_rounds(self):
        JudgingRound = swapper.load_model('accelerator', 'JudgingRound')
        judge_grants = self.user.programrolegrant_set.filter(
            program_role__user_role__name=UserRole.JUDGE)
        program_ids = judge_grants.values_list('program_role__program_id')
        rounds = JudgingRound.objects.filter(
            is_active=True,
            program_id__in=program_ids)
        return rounds

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

    def get_deadline(self, judging_round):
        if judging_round and judging_round.end_date_time:
            return judging_round.end_date_time
        else:
            return "N/A"

    def get_current_quota(self, judging_round):
        current_quota = 0
        commitment = self.get_commitment(judging_round)
        try:
            current_quota = commitment.current_quota or 0
        except AttributeError:
            pass
        finally:
            return current_quota

    def get_commitment(self, judging_round):
        if judging_round:
            return self.user.judgeroundcommitment_set.filter(
                judging_round=judging_round).first()
        else:
            return None

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
                completed_count = _get_completed_application_count(
                    forms, completed_count, assignment_completed, application)
        return app_count, completed_count

    def is_judge(self, program=None, state=None):
        """If program is specified, is the user a judge in that program.
        Otherwise, is the user a judge in any program."""
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


def _get_office_hour_holder_active_programs(user):
    Clearance = swapper.load_model('accelerator', 'Clearance')
    clearances = Clearance.objects.clearances_for_user(user).filter(
        program_family__programs__program_status=ACTIVE_PROGRAM_STATUS)
    active_program_ids = set()
    active_program_ids.update(list(clearances.values_list(
        'program_family__programs__id', flat=True
    ).distinct()))
    active_program_ids.update(list(user.programrolegrant_set.filter(
        OFFICE_HOURS_HOLDER & ACTIVE_PROGRAM
    ).values_list('program_role__program__id', flat=True).distinct()))
    return active_program_ids


def _get_completed_application_count(
        forms, completed_count, assignment_completed, application):
    if assignment_completed:
        form = forms.get(str(application.pk), None)
        if form and form.feedback_status != 'INCOMPLETE':
            completed_count += 1
    return completed_count
