import uuid

from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone

from accelerator_abstract.models import BaseUserRole
from accelerator_abstract.models.base_base_profile import EXPERT_USER_TYPE


MAX_USERNAME_LENGTH = 30


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves an User with the given email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('An email address must be provided.')
        email = self.normalize_email(email)
        if "is_active" not in extra_fields:
            extra_fields["is_active"] = True
        if "username" not in extra_fields:
            # For now we need to have a unique id that is at
            # most 30 characters long.  Using uuid and truncating.
            # Ideally username goes away entirely at some point
            # since we're really using email.  If we have to keep
            # username for some reason then we could switch over
            # to a string version of the pk which is guaranteed
            # be unique.
            extra_fields["username"] = str(uuid.uuid4())[:MAX_USERNAME_LENGTH]
        user = self.model(email=email,
                          is_staff=is_staff,
                          is_superuser=is_superuser,
                          last_login=None,
                          date_joined=now,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True,
                                 **extra_fields)


class User(AbstractUser):
    # Override the parent email field to add uniqueness constraint
    email = models.EmailField(blank=True, unique=True)

    objects = UserManager()

    class Meta:
        db_table = 'auth_user'
        managed = settings.ACCELERATOR_MODELS_ARE_MANAGED

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self.startup = None
        self.team_member = None
        self.profile = None
        self.user_finalist_roles = None

    class AuthenticationException(Exception):
        pass

    def __str__(self):
        return self.email

    def full_name(self):
        fn = self.first_name
        ln = self.last_name
        if fn and ln:
            name = u"%s %s" % (fn, ln)
        else:
            name = str(self.email)
        return name

    def user_phone(self):
        return self._get_profile().phone

    def image_url(self):
        return self._get_profile().image_url()

    def team_member_id(self):
        return self.team_member.id if self._get_member() else ''

    def user_title(self):
        return self._get_title_and_company()['title']

    def user_twitter_handle(self):
        return self._get_profile().twitter_handle

    def user_linked_in_url(self):
        return self._get_profile().linked_in_url

    def user_facebook_url(self):
        return self._get_profile().facebook_url

    def user_personal_website_url(self):
        return self._get_profile().personal_website_url

    def type(self):
        return self._get_profile().user_type

    def startup_name(self):
        return self._get_title_and_company()['company']

    def _get_title_and_company(self):
        if self._is_expert() and self._has_expert_details():
            profile = self._get_profile()
            title = profile.title
            company = profile.company
            return {
                "title": title,
                "company": company
            }
        self._get_member()
        title = self.team_member.title if self.team_member else ""
        company = self.startup.name if self._get_startup() else None
        return {
            "title": title,
            "company": company
        }

    def _has_expert_details(self):
        if self._is_expert():
            profile = self._get_profile()
            return True if profile.title or profile.company else False

    def startup_industry(self):
        return self.startup.primary_industry if self._get_startup() else None

    def top_level_startup_industry(self):
        industry = (
            self.startup.primary_industry if self._get_startup() else None)
        return industry.parent if industry and industry.parent else industry

    def startup_status_names(self):
        if self._get_startup():
            return [startup_status.program_startup_status.startup_status
                    for startup_status in self.startup.startupstatus_set.all()]

    def finalist_user_roles(self):
        if not self.user_finalist_roles:
            finalist_roles = BaseUserRole.FINALIST_USER_ROLES
            self.user_finalist_roles = self.programrolegrant_set.filter(
                program_role__user_role__name__in=finalist_roles
            ).values_list('program_role__name', flat=True).distinct()
        return list(self.user_finalist_roles)

    def program(self):
        return self.startup.current_program() if self._get_startup() else None

    def location(self):
        program = self.program()
        return program.program_family.name if program else None

    def year(self):
        program = self.program()
        return program.start_date.year if program else None

    def is_team_member(self):
        return True if self._get_member() else False

    def _get_startup(self):
        if not self.startup:
            self._get_member()
            if self.team_member:
                self.startup = self.team_member.startup
        return self.startup

    def _get_member(self):
        if not self.team_member:
            self.team_member = self.startupteammember_set.last()
        return self.team_member

    def _get_profile(self):
        if self.profile:
            return self.profile
        self.profile = self.get_profile()
        return self.profile

    def has_a_finalist_role(self):
        return len(self.finalist_user_roles()) > 0

    def _is_expert(self):
        profile = self._get_profile()
        return profile.user_type == EXPERT_USER_TYPE.lower()
