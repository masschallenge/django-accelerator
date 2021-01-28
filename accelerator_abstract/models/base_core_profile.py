# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from datetime import datetime
from pytz import utc

import swapper
from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models
from django.db.models import Q
from sorl.thumbnail import ImageField

from accelerator.utils import flag_smith_has_feature
from accelerator_abstract.models.accelerator_model import AcceleratorModel
from accelerator_abstract.models.base_user_role import (
    BaseUserRole,
)
from accelerator_abstract.models.base_base_profile import (
    EXPERT_USER_TYPE,
)
from accelerator_abstract.models.base_user_utils import (
    has_staff_clearance,
)
from accelerator_abstract.models.base_program import (
    ACTIVE_PROGRAM_STATUS,
    ENDED_PROGRAM_STATUS,
)

GENDER_MALE_CHOICE = ('m', 'Male')
GENDER_FEMALE_CHOICE = ('f', 'Female')
GENDER_OTHER_CHOICE = ('o', 'Other')
GENDER_PREFER_NOT_TO_STATE_CHOICE = ('p', 'Prefer Not To State')
GENDER_UNKNOWN_CHOICE = ('', 'Unknown')

GENDER_CHOICES = (
    GENDER_FEMALE_CHOICE,
    GENDER_MALE_CHOICE,
    GENDER_PREFER_NOT_TO_STATE_CHOICE,
    GENDER_OTHER_CHOICE,
    GENDER_UNKNOWN_CHOICE,
)

UI_GENDER_CHOICES = (
    GENDER_FEMALE_CHOICE,
    GENDER_MALE_CHOICE,
    GENDER_PREFER_NOT_TO_STATE_CHOICE,
    GENDER_OTHER_CHOICE,
)
JUDGE_FIELDS_TO_LABELS = {'desired_judge_label': 'Desired Judge',
                          'confirmed_judge_label': 'Judge'}
EXPERT_NAVIGATION_EPIC = "expert_navigation"


class BaseCoreProfile(AcceleratorModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default='')
    gender_identity = models.ManyToManyField(
        swapper.get_model_name(
            AcceleratorModel.Meta.app_label, 'GenderChoices'),
        blank=True
    )
    gender_self_description = models.TextField(blank=True, default="")
    phone = models.CharField(
        verbose_name="Phone",
        max_length=20,
        validators=[RegexValidator(
            regex='^[0-9x.+() -]+$',
            message='Digits and +()-.x only')],
        blank=True)
    linked_in_url = models.URLField(
        verbose_name="LinkedIn profile URL",
        blank=True)
    facebook_url = models.URLField(
        verbose_name="Facebook profile URL",
        blank=True)
    twitter_handle = models.CharField(
        verbose_name="Twitter handle",
        max_length=40,
        blank=True)
    personal_website_url = models.URLField(
        verbose_name="Website URL",
        max_length=255,
        blank=True)
    landing_page = models.CharField(
        verbose_name="Current landing page within the site",
        validators=[RegexValidator(
            "^[^:]*$",
            "Must be a page within the site"), ],
        max_length=200,
        blank=True)
    image = ImageField(
        upload_to='profile_pics',
        verbose_name="Profile Picture",
        help_text="Suggested size: <400px on the short side",
        blank=True)
    drupal_id = models.IntegerField(blank=True, null=True)
    drupal_creation_date = models.DateTimeField(blank=True, null=True)
    drupal_last_login = models.DateTimeField(blank=True, null=True)
    interest_categories = models.ManyToManyField(
        to=swapper.get_model_name(AcceleratorModel.Meta.app_label,
                                  'InterestCategory'),
        blank=True)
    users_last_activity = models.DateTimeField(blank=True, null=True)
    current_program = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               'Program'),
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    program_families = models.ManyToManyField(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               'ProgramFamily'),
        help_text="Which of our Program Families would you like to be "
                  "involved with?",
        related_name="interested_%(class)s",
        blank=True
    )

    user_type = None
    default_page = "member_homepage"
    newsletter_sender = models.BooleanField(default=False)
    birth_year = models.DateField(blank=True, null=True)
    ethno_racial_identification = models.ManyToManyField(
        swapper.get_model_name(
            AcceleratorModel.Meta.app_label, 'EthnoRacialIdentity'
        ),
        blank=True,
    )
    authorization_to_share_ethno_racial_identity = models.BooleanField(
        default=False,
    )

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_coreprofile'
        abstract = True

    def __str__(self):
        identifier = self.full_name()
        ptype = ''
        if self.user_type is not None:
            ptype = ("%s " % self.user_type).title()
        return "%sProfile for %s" % (ptype, identifier)

    def full_name(self):
        return self.user.full_name()

    def image_url(self):
        if str(self.image):
            return self.image.storage.url(
                self.image.name)
        else:
            return ""

    def is_judge(self, *args, **kwargs):
        """prevent attribute errors on subclasses
        """
        return False

    def is_program_graduate(self, program=None):
        """ This checks if the user is an alumni or graduate of the program
        """
        qs = self.user.programrolegrant_set.filter(
            program_role__user_role__name=BaseUserRole.FINALIST,
            program_role__program__program_status=ENDED_PROGRAM_STATUS)
        if program:
            qs = qs.filter(program_role__program=program)
        return qs.exists()

    def is_alum_in_residence(self):
        return self.user.programrolegrant_set.filter(
            program_role__user_role__name=BaseUserRole.AIR
        ).exists()

    def is_mentor(self, program=None):
        """If program is specified, is the expert a mentor in that program.
        Otherwise, is the expert a mentor in any program.
        """
        if program:
            return self.user.programrolegrant_set.filter(
                program_role__program__exact=program,
                program_role__user_role__name=BaseUserRole.MENTOR).exists()
        else:
            return self.user.programrolegrant_set.filter(
                program_role__user_role__name=BaseUserRole.MENTOR).exists()

    def user_roles(self):
        return set([prg.program_role.user_role
                    for prg in self.user.programrolegrant_set.all()
                    if prg.program_role.user_role is not None])

    def is_office_hour_holder(self):
        user_role_names = set([ur.name for ur in self.user_roles()])
        return len(user_role_names.intersection(
            BaseUserRole.OFFICE_HOUR_ROLES)) > 0

    def is_partner(self):
        PartnerTeamMember = swapper.load_model(
            'accelerator', 'PartnerTeamMember')
        return PartnerTeamMember.objects.filter(
            team_member=self.user).exists()

    def is_partner_admin(self):
        PartnerTeamMember = swapper.load_model(
            'accelerator', 'PartnerTeamMember')
        return PartnerTeamMember.objects.filter(
            team_member=self.user,
            partner_administrator=True).exists()

    def get_active_alerts(self, page=None):
        """Return any active alerts for the user, that are relevant for
        the current 'page' of the application.
        May be overridden by subclasses (e.g., ExpertProfile,
        EntrepreneurProfile, etc.)
        """
        alerts = []
        return alerts

    def _get_staff_landing_page(self):
        if has_staff_clearance(self.user):
            return '/staff'

    def role_based_landing_page(self, exclude_role_names=[]):
        if flag_smith_has_feature(EXPERT_NAVIGATION_EPIC):
            if self.user_type.upper() == EXPERT_USER_TYPE:
                return "/dashboard/expert/overview/"
        JudgingRound = swapper.load_model(AcceleratorModel.Meta.app_label,
                                          "JudgingRound")
        UserRole = swapper.load_model(
            'accelerator', 'UserRole')
        now = utc.localize(datetime.now())
        active_judging_round_labels = JudgingRound.objects.filter(
            end_date_time__gt=now,
            is_active=True).values_list("confirmed_judge_label",
                                        flat=True)
        active_judge_grants = Q(
            program_role__user_role__name=UserRole.JUDGE,
            program_role__user_label_id__in=active_judging_round_labels)

        desired_judging_round_labels = JudgingRound.objects.filter(
            end_date_time__gt=now).values_list("desired_judge_label",
                                               flat=True)
        desired_judge_grants = Q(
            program_role__user_role__name=UserRole.DESIRED_JUDGE,
            program_role__user_label__in=desired_judging_round_labels
        )

        active_mentor_grants = Q(
            program_role__user_role__name=UserRole.MENTOR,
            program_role__program__program_status=ACTIVE_PROGRAM_STATUS
        )
        REMAINING_ROLES = UserRole.objects.exclude(
            name__in=[UserRole.JUDGE,
                      UserRole.DESIRED_JUDGE,
                      UserRole.MENTOR]).values_list("name", flat=True)
        remaining_grants = Q(
            program_role__user_role__name__in=REMAINING_ROLES,
            program_role__user_role__isnull=False,
            program_role__landing_page__isnull=False)
        query = self.user.programrolegrant_set.filter(
            active_judge_grants |
            desired_judge_grants |
            active_mentor_grants |
            remaining_grants).exclude(
                program_role__landing_page="").exclude(
                    program_role__landing_page__isnull=True)

        if exclude_role_names:
            query = query.exclude(
                program_role__user_role__name__in=exclude_role_names)
        grant = query.order_by("-program_role__program__end_date",
                               "program_role__user_role__sort_order"
                               ).first()
        if grant:
            return grant.program_role.landing_page
        return self.default_page

    def calc_landing_page(self):
        return (
            self._get_staff_landing_page() or
            self.role_based_landing_page())

    def check_landing_page(self):
        page = self.landing_page or self.calc_landing_page()
        if page == "/":
            return self.default_page
        return page

    def first_startup(self, statuses=[]):
        return None

    def interest_category_names(self):
        return [interest.name for interest in self.interest_categories.all()]

    def program_family_names(self):
        return [pf.name for pf in self.program_families.all()]

    def gender_value(self):
        gender_dict = dict(GENDER_CHOICES)
        return gender_dict[self.gender.lower()]

    def confirmed_mentor_programs(self):
        return list(self.user.programrolegrant_set.filter(
            program_role__user_role__name=BaseUserRole.MENTOR).values_list(
            'program_role__program__name', flat=True))

    def confirmed_memtor_program_families_all(self):
        return list(self.user.programrolegrant_set.filter(
            program_role__user_role__name=BaseUserRole.MENTOR).values_list(
                "program_role__program__program_family__name", flat=True
        ).distinct())
