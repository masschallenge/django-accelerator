import swapper
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
    ENDED_PROGRAM_STATUS,
    HIDDEN_PROGRAM_STATUS,
    UPCOMING_PROGRAM_STATUS,
)
from accelerator_abstract.models.base_core_profile import BaseCoreProfile
from accelerator_abstract.models.base_user_utils import is_employee

SHORT_BIO_MAX_LENGTH = 140
OFFICE_HOUR_HOLDER_ROLES = [UserRole.MENTOR, UserRole.AIR]
OFFICE_HOURS_HOLDER = Q(
    program_role__user_role__name__in=OFFICE_HOUR_HOLDER_ROLES)
ACTIVE_PROGRAM = Q(program_role__program__program_status='active')


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
