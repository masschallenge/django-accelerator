from datetime import datetime
from decimal import Decimal
from pytz import utc

import swapper
from django.conf import settings
from django.core.validators import (
    RegexValidator,
    MaxLengthValidator,
)
from django.db import models
from django.db.models import Q
from sorl.thumbnail import ImageField
from django.utils.safestring import mark_safe

from accelerator_abstract.models.accelerator_model import AcceleratorModel
from accelerator_abstract.models.base_user_role import (
    BaseUserRole,
)
from accelerator_abstract.models.base_base_profile import (
    EXPERT_USER_TYPE,
    ENTREPRENEUR_USER_TYPE,
)
from accelerator_abstract.models.base_user_utils import (
    has_staff_clearance,
)
from accelerator_abstract.models.base_program import (
    ACTIVE_PROGRAM_STATUS,
    ENDED_PROGRAM_STATUS,
)
from accelerator.utils import flag_smith_has_feature

INVITED_JUDGE_ALERT = (
    "<h4>{first_name}, we would like to invite you to be a judge at "
    "MassChallenge!</h4>"
    "<p>&nbsp;</p>"
    "<p>{round_name} judging occurs from {start_date} to {end_date}! "
    "Of all our potential judges, we would like you, {first_name}, "
    "to take part."
    "</p><p>&nbsp;</p>"
    '<p><a class="btn btn-primary" href="/expert/commitments/">Click '
    "here to tell us your availability"
    "</a></p> <p>&nbsp;</p>"
)

MENTOR_TYPE_HELPTEXT = (
    "Allowed Values: "
    "F - Functional Expert, "
    "P - Partner, "
    "T - Technical, "
    "E - Entrepreneur, "
    "N - Once accepted, now rejected, "
    "X - Not Accepted as a Mentor (may still be a judge)")

JUDGE_TYPE_HELPTEXT = (
    "Allowed Values: "
    "1 - Round 1 Judge, "
    "2 - Round 2 Judge, "
    "3 - Pre-final Judge, "
    "4 - Final Judge, "
    "0 - Once Accepted, now rejected, "
    "X - Not Accepted as a Judge (May still be a mentor)")

IDENTITY_HELP_TEXT_VALUE = (mark_safe(
            'Select as many options as you feel best represent your identity. '
            'Please press and hold Control (CTRL) on PCs or '
            'Command (&#8984;) on Macs to select multiple options'))

JUDGE_FIELDS_TO_LABELS = {'desired_judge_label': 'Desired Judge',
                          'confirmed_judge_label': 'Judge'}
BIO_MAX_LENGTH = 7500

PRIVACY_KEY_STAFF = "staff"
PRIVACY_KEY_FINALISTS_AND_STAFF = "finalists and staff"
PRIVACY_KEY_PUBLIC = "public"

PRIVACY_CHOICES = ((PRIVACY_KEY_STAFF, "MC Staff Only"),
                   (PRIVACY_KEY_FINALISTS_AND_STAFF, "Finalists and MC Staff"),
                   (PRIVACY_KEY_PUBLIC, "All Users"),)

BASE_INTEREST = "I would like to participate in MassChallenge %s"
BASE_TOPIC = ("Please describe the topic(s) you would be available "
              "to speak%s about%s")

REF_BY_TEXT = ("If someone referred you to MassChallenge, please provide "
               "their name (and organization if relevant). Otherwise, please "
               "indicate how you learned about the opportunity to participate "
               "at MassChallenge (helps us understand the effectiveness of "
               "our outreach programs).")
OTHER_EXPERTS_TEXT = ("We're always looking for more great experts to join "
                      "the MassChallenge community and program. We welcome "
                      "the names and contact info (email) of individuals you "
                      "think could be great additions to the program, as well "
                      "as how you think they might want to be involved "
                      "(Judge, Mentor, etc.) Also, please encourage these "
                      "individuals to fill out their own Expert Profile.")
PRONOUN_CHOICES = (
    ('she, her, hers', 'She, Her, Hers'),
    ("he, him, his", "He, Him, His"),
    ("they, them, theirs", "They, Them, Theirs"),
    ('Just my name please!', "Just my name please!"),
    ("other", "Other"),)

EDUCATIONAL_LEVEL_CHOICES = (
    ("No formal schooling", "No formal schooling"),
    ("Completed high school", "Completed high school"),
    ("Associates degree (for example: AA, AS)",
     "Associates degree (for example: AA, AS)"),
    ("Bachelor’s degree (for example: BA. BS)",
     "Bachelor’s degree (for example: BA. BS)"),
    ("Professional degree (for example: MD, DDS, DVM, LLB, JD)",
     "Professional degree (for example: MD, DDS, DVM, LLB, JD)"),
    ("Advanced degree (Masters or Doctoral)",
     "Advanced degree (Masters or Doctoral)"),)

HERE_ABOUT_US_CHOICES = (
    ("Advertising", "Advertising"),
    ("Email from MassChallenge", "Email from MassChallenge"),
    ("Search engine (Google, Yahoo, etc.)",
     "Search engine (Google, Yahoo, etc.)"),
    ("Recommended by friend or colleague",
     "Recommended by friend or colleague"),
    ("Recommended by a community organization",
     "Recommended by a community organization"),
    ("Social media", "Social media"),
    ("Blog or publication", "Blog or publication"),
    ("Other", "Other"),)

GEOGRAPHIC_EXPERIENCE_HELP_TEXT = (
    mark_safe('You may select up to 5 regions. To select multiple '
              'regions, please press and hold Control (CTRL) on PCs '
              'or Command (&#8984;) on Macs'))


LANDING_PAGE_MAP = {
    EXPERT_USER_TYPE: 'expert_homepage',
    ENTREPRENEUR_USER_TYPE: 'profile',}


class BaseCoreProfile(AcceleratorModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    gender_identity = models.ManyToManyField(
        swapper.get_model_name(
            AcceleratorModel.Meta.app_label, 'GenderChoices'),
        help_text=IDENTITY_HELP_TEXT_VALUE,
        blank=True)
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
        help_text=IDENTITY_HELP_TEXT_VALUE
    )
    authorization_to_share_ethno_racial_identity = models.BooleanField(
        default=False,
    )
    bio = models.TextField(blank=True,
                           default="",
                           validators=[MaxLengthValidator(BIO_MAX_LENGTH)])

    title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Professional Title")
    company = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Company Name")
    expert_category = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               "ExpertCategory"),
        verbose_name="My background is primarily as a(n)",
        related_name="%(class)s_experts",
        blank=True, null=True,  # added
        on_delete=models.CASCADE)
    primary_industry = models.ForeignKey(
        settings.MPTT_SWAPPABLE_INDUSTRY_MODEL,
        verbose_name="Primary Industry/Experience",
        related_name="%(class)s_experts",
        limit_choices_to={'level__exact': 0},
        null=True,
        blank=True,
        on_delete=models.CASCADE)
    additional_industries = models.ManyToManyField(
        settings.MPTT_SWAPPABLE_INDUSTRY_MODEL,
        verbose_name="Additional Industries",
        help_text=(mark_safe(
            'You may select up to 5 related industries. To select multiple '
            'industries, please press and hold Control (CTRL) on PCs or '
            'Command (&#8984;) on Macs.')),
        related_name="%(class)s_secondary_experts",
        blank=True,
    )
    functional_expertise = models.ManyToManyField(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               'FunctionalExpertise'),
        verbose_name="Functional Expertise",
        related_name="%(class)s_experts",
        blank=True)
    public_website_consent = models.BooleanField(
        verbose_name="Public Website Consent",
        blank=False,
        null=False,
        default=False)
    privacy_email = models.CharField(
        max_length=64,
        verbose_name="Privacy - Email",
        choices=PRIVACY_CHOICES,
        blank=True,
        default=PRIVACY_CHOICES[1][0])
    privacy_phone = models.CharField(
        max_length=64,
        verbose_name="Privacy - Phone",
        choices=PRIVACY_CHOICES,
        blank=True,
        default=PRIVACY_CHOICES[1][0])
    privacy_web = models.CharField(
        max_length=64,
        verbose_name="Privacy - Web",
        choices=PRIVACY_CHOICES,
        blank=True,
        default=PRIVACY_CHOICES[1][0])
    home_program_family = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               "ProgramFamily"),
        verbose_name="Home Program Family",
        blank=True,
        null=True,
        on_delete=models.CASCADE)
    judge_interest = models.BooleanField(
        verbose_name="Judge",
        help_text=BASE_INTEREST % 'as a Judge',
        default=False)
    mentor_interest = models.BooleanField(
        verbose_name="Mentor",
        help_text=BASE_INTEREST % 'as a Mentor',
        default=False)
    speaker_interest = models.BooleanField(
        verbose_name="Speaker",
        help_text=BASE_INTEREST % 'as a Speaker',
        default=False)
    speaker_topics = models.TextField(
        verbose_name="Speaker Topics",
        help_text=BASE_TOPIC % ('', ''),
        blank=True)
    office_hours_interest = models.BooleanField(
        verbose_name="Office Hours",
        help_text=BASE_INTEREST % 'by holding Office Hours',
        default=False)
    office_hours_topics = models.TextField(
        verbose_name="Office Hour Topics",
        help_text=BASE_TOPIC % (' to Finalists', ' during Office Hours'),
        blank=True)
    referred_by = models.TextField(
        max_length=500,
        blank=True,
        help_text=REF_BY_TEXT)
    other_potential_experts = models.TextField(
        max_length=500,
        blank=True,
        help_text=OTHER_EXPERTS_TEXT)
    salutation = models.CharField(
        max_length=255,
        blank=True)
    mentor_type = models.CharField(
        max_length=1,
        blank=True,
        help_text=MENTOR_TYPE_HELPTEXT,
        verbose_name="Mentor Type")
    judge_type = models.CharField(
        max_length=1,
        blank=True,
        help_text=JUDGE_TYPE_HELPTEXT,
        verbose_name="Judge Type")
    public_website_consent_checked = models.BooleanField(
        verbose_name="Public Website Consent Check",
        blank=False,
        null=False,
        default=False)
    mentoring_specialties = models.ManyToManyField(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               'MentoringSpecialties'),
        verbose_name="Mentoring Specialties",
        help_text='Hold down "Control", or "Command" on a Mac,'
                  'to select more than one.',
        related_name="%(class)s_experts",
        blank=True)
    expert_group = models.CharField(
        verbose_name="Expert Group",
        max_length=10,
        blank=True)
    preferred_name = models.CharField(
        verbose_name="Nickname / Preferred Name",
        max_length=32,
        null=True,
        blank=True)
    pronouns = models.CharField(
        verbose_name="Pronouns",
        max_length=32,
        choices=PRONOUN_CHOICES,
        null=True,
        blank=True)
    education_level = models.CharField(
        verbose_name="Education Level",
        max_length=200,
        choices=EDUCATIONAL_LEVEL_CHOICES,
        null=True,
        blank=True)
    here_about_us = models.CharField(
        verbose_name="Where did you here about us",
        max_length=100,
        choices=HERE_ABOUT_US_CHOICES,
        null=True,
        blank=True)
    expert_interest = models.BooleanField(
        verbose_name="Expert Interest",
        default=False)
    entrepreneur_interest = models.BooleanField(
        verbose_name="Enterpreneur Interest",
        default=False)
    worldwide_participation_interest = models.BooleanField(
        verbose_name="World Wide Participation Interest",
        default=False)
    shared_demographic_data = models.BooleanField(
        verbose_name="Permission To Shared Demographic Data",
        default=False)
    user_location = models.OneToOneField(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               'Location'),
        on_delete=models.CASCADE,
        null=True,
        blank=True)
    reliability = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=Decimal("1.00"),
        blank=True,
        null=True)
    internal_notes = models.TextField(
        max_length=500,
        blank=True,
        help_text="Internal notes only for use by MassChallenge Staff "
                  "(not visible to Expert)")
    community_participation = models.ManyToManyField(
        'CommunityParticipation',
        blank=True,
        related_name='profiles')
    geographic_experience = models.ManyToManyField(
        'GeographicExperience',
        verbose_name="Geographic Experience/Expertise",
        help_text=GEOGRAPHIC_EXPERIENCE_HELP_TEXT,
        blank=True)
    privacy_profile = models.CharField(
        max_length=64,
        verbose_name="Privacy - Profile",
        choices=PRIVACY_CHOICES,
        blank=True,
        default=PRIVACY_CHOICES[1][0])
    program_location_interest = models.ManyToManyField(
        swapper.get_model_name(
            AcceleratorModel.Meta.app_label, 'ProgramFamilyLocation'),
        blank=True,
        related_name='profiles')
    program_interest = models.ManyToManyField(
        swapper.get_model_name(
            AcceleratorModel.Meta.app_label, 'Program'),
        blank=True,
        related_name='profiles')
    innovation_stage_interest = models.ManyToManyField(
        swapper.get_model_name(
            AcceleratorModel.Meta.app_label, 'InnovationStage'),
        blank=True,
        related_name='profiles')
    industry_cluster_interest = models.ManyToManyField(
        swapper.get_model_name(
            AcceleratorModel.Meta.app_label, 'IndustryCluster'),
        blank=True, related_name='profiles')

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

    def is_alum_in_residence(self, program=None):
        qs = self.user.programrolegrant_set.filter(
            program_role__user_role__name=BaseUserRole.AIR)
        if program:
            qs = qs.filter(program_role__program=program)
        return qs.exists()

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
        """no op
        """
        return []

    def _get_staff_landing_page(self):
        if has_staff_clearance(self.user):
            return '/staff'

    def role_based_landing_page(self, exclude_role_names=[]):
        if self.participation.upper() == EXPERT_USER_TYPE:
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
        return self.user_default_page

    def calc_landing_page(self):
        return (
            self._get_staff_landing_page() or
            self.role_based_landing_page())

    def check_landing_page(self):
        page = self.landing_page or self.calc_landing_page()
        if page == "/":
            return self.user_default_page
        return page

    def first_startup(self, statuses=[]):
        startup_memberships = self.user.startupteammember_set.order_by(
            '-startup__created_datetime')
        if statuses:
            startup_memberships = startup_memberships.filter(
                startup__startupstatus__program_startup_status__in=statuses)
        if startup_memberships:
            return startup_memberships.first().startup
        return None

    def interest_category_names(self):
        return [interest.name for interest in self.interest_categories.all()]

    def program_family_names(self):
        program_roles = self.user.programrolegrant_set.filter(
            program_role__user_role__name__in=[BaseUserRole.FINALIST,
                                               BaseUserRole.ALUM,
                                               BaseUserRole.MENTOR])
        return list(program_roles.values_list(
            'program_role__program__program_family__name',
            flat=True).distinct())

    def confirmed_mentor_programs(self):
        return list(self.user.programrolegrant_set.filter(
            program_role__user_role__name=BaseUserRole.MENTOR).values_list(
            'program_role__program__name', flat=True))

    def confirmed_memtor_program_families_all(self):
        return list(self.user.programrolegrant_set.filter(
            program_role__user_role__name=BaseUserRole.MENTOR).values_list(
                "program_role__program__program_family__name", flat=True
        ).distinct())

    @property
    def participation(self):
        """
        returns the user type representation for users without user_type
        profile objects
        """
        user_type_representation = self.user_type
        if not self.user_type:
            if self.expert_interest:
                user_type_representation = EXPERT_USER_TYPE
            if self.entrepreneur_interest:
                user_type_representation = ENTREPRENEUR_USER_TYPE
        return user_type_representation

    @property
    def user_default_page(self):
        url_map = LANDING_PAGE_MAP
        try:
            return url_map[self.participation.upper()]
        except KeyError:
            return self.default_page
