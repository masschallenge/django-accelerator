# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from simpleuser.models import User

from .allocator import Allocator
from .startup_role import StartupRole
from .user_role import UserRole
from .user_role_menu import UserRoleMenu
from .program_cycle import ProgramCycle
from .base_profile import (
    BaseProfile,
)
from accelerator_abstract.models.base_base_profile import (
    PHONE_MAX_LENGTH,
    TWITTER_HANDLE_MAX_LENGTH,
    USER_TYPES,
    ENTREPRENEUR_USER_TYPE,
    MEMBER_USER_TYPE,
    EXPERT_USER_TYPE,
)
from .criterion import Criterion
from .criterion_option_spec import CriterionOptionSpec
from .currency import Currency
from .program import Program
from accelerator_abstract.models.base_program import (
    ACTIVE_PROGRAM_STATUS,
    CURRENT_STATUSES,
    ENDED_PROGRAM_STATUS,
    HIDDEN_PROGRAM_STATUS,
    UPCOMING_PROGRAM_STATUS,
)

from .model_change import ModelChange
from accelerator_abstract.models.base_model_change import (
    MIGRATION_STATUS_DONE,
    MIGRATION_STATUS_ERROR,
    MIGRATION_STATUS_MIGRATING,
    MIGRATION_STATUS_OLD,
)
from .program_startup_status import ProgramStartupStatus
from accelerator_abstract.models.base_program_startup_status import (
    STARTUP_BADGE_DISPLAY_VALUES
)

from .startup_program_interest import StartupProgramInterest
from accelerator_abstract.models.base_startup_program_interest import (
    INTEREST_CHOICES
)
from .startup_cycle_interest import StartupCycleInterest
from .recommendation_tag import RecommendationTag

from .site import Site
from .site_program_authorization import SiteProgramAuthorization
from .mentor_program_office_hour import MentorProgramOfficeHour

from accelerator_abstract.models.base_mentor_program_office_hour import (
    LOCATION_CHOICES,
    MC_BOS_LOCATION,
    MC_CH_LOCATION,
    MC_IL_JLM_LOCATION,
    MC_OTHER_LOCATION,
    MC_MX_LOCATION,
    MC_NIC_LOCATION,
    MC_PULSE_LOCATION,
    MC_REMOTE_LOCATION,
)
from .program_override import ProgramOverride
from .refund_code import RefundCode
from .observer import Observer
from .program_family import ProgramFamily
from .entrepreneur_profile import EntrepreneurProfile
from .expert_profile import ExpertProfile
from accelerator_abstract.models.base_expert_profile import BIO_MAX_LENGTH
from .functional_expertise import FunctionalExpertise
from .industry import Industry
from .member_profile import MemberProfile
from .named_group import NamedGroup
from .organization import Organization
from accelerator_abstract.models.base_organization import slug_from_instance
from .partner import Partner
from .partner_team_member import PartnerTeamMember
from .program_role import ProgramRole
from .program_role_grant import ProgramRoleGrant
from .expert_interest import ExpertInterest
from .startup import Startup
from accelerator_abstract.models.base_startup import (
    STARTUP_COMMUNITIES,
    DEFAULT_PROFILE_BACKGROUND_COLOR,
    DEFAULT_PROFILE_TEXT_COLOR,
)
from .application_type import ApplicationType
from .question import Question
from accelerator_abstract.models.base_question import (
    CHOICE_LAYOUT_HORIZONTAL,
    CHOICE_LAYOUT_VERTICAL,
    CHOICE_LAYOUT_DROPDOWN,
    CHOICE_LAYOUTS,
    QUESTION_TYPE_MULTILINE,
    QUESTION_TYPE_MULTICHOICE,
    QUESTION_TYPE_NUMBER,
    QUESTION_TYPES,
)
from .application_question import ApplicationQuestion
from accelerator_abstract.models.base_application_question import (
    TEXT_LIMIT_UNITS,
)
from .application_answer import ApplicationAnswer
from .application import Application
from accelerator_abstract.models.base_application import (
    APPLICATION_STATUSES,
    COMPLETE_APP_STATUS,
    DELAYED_STATUS,
    ERROR_PAYMENT_STATUS,
    FAILED_STATUS,
    INCOMPLETE_APP_STATUS,
    INSTANT_STATUS,
    NOT_ELIGIBLE_STATUS,
    PAID_PAYMENT_STATUS,
    PAYMENT_STATUSES,
    REFUND_STATUSES,
    REQUIRED_STATUS,
    SUBMITTED_APP_STATUS,
    UNPAID_PAYMENT_STATUS,
)

from .clearance import Clearance
from accelerator_abstract.models.base_clearance import (
    CLEARANCE_LEVEL_EXEC_MD,
    CLEARANCE_LEVEL_GLOBAL_MANAGER,
    CLEARANCE_LEVEL_POM,
    CLEARANCE_LEVELS,
)

from .refund_code_redemption import RefundCodeRedemption
from .reference import Reference
from .startup_team_member import StartupTeamMember

from .program_startup_attribute import ProgramStartupAttribute
from .startup_attribute import StartupAttribute
from .startup_override_grant import StartupOverrideGrant
from .startup_status import StartupStatus
from .startup_mentor_tracking_record import (
    StartupMentorTrackingRecord,
)
from .startup_mentor_relationship import StartupMentorRelationship
from accelerator_abstract.models.base_startup_mentor_relationship import (
    CONFIRMED_RELATIONSHIP,
    DESIRED_RELATIONSHIP,
    DISCUSSING_RELATIONSHIP,
    RELATIONSHIP_CHOICES,
)
from .interest_category import InterestCategory
from .expert_category import ExpertCategory
from accelerator_abstract.models.base_expert_category import (
    VALID_EXPERT_CATEGORIES
)
from .expert_interest_type import ExpertInterestType
from .job_posting import JobPosting
from accelerator_abstract.models.base_job_posting import JOB_TYPE_VALUES
from .newsletter_receipt import NewsletterReceipt
from .newsletter import Newsletter
from .section import Section
from accelerator_abstract.models.base_section import INCLUDE_FOR_CHOICES
from .program_partner import ProgramPartner
from .program_partner_type import ProgramPartnerType
from accelerator_abstract.models.base_program_partner_type import (
    PARTNER_BADGE_DISPLAY_VALUES
)
from .site import Site
from .judging_form import JudgingForm

from .judge_application_feedback import JudgeApplicationFeedback
from accelerator_abstract.models.base_judge_application_feedback import (
    JUDGING_FEEDBACK_STATUS_COMPLETE,
    JUDGING_FEEDBACK_STATUS_CONFLICT,
    JUDGING_FEEDBACK_STATUS_ENUM,
    JUDGING_FEEDBACK_STATUS_INCOMPLETE,
    JUDGING_FEEDBACK_STATUS_OTHER,
    JUDGING_STATUS_CONFLICT,
    JUDGING_STATUS_ENUM,
    JUDGING_STATUS_NO_CONFLICT,
    JUDGING_STATUS_OTHER,
)
from .judge_availability import JudgeAvailability
from accelerator_abstract.models.base_judge_availability import (
    JUDGE_AVAILABILITY_AVAILABLE,
    JUDGE_AVAILABILITY_NOT_AVAILABLE,
    JUDGE_AVAILABILITY_PREFERRED,
)
from .judge_panel_assignment import JudgePanelAssignment
from accelerator_abstract.models.base_judge_panel_assignment import (
    ASSIGNED_PANEL_ASSIGNMENT_STATUS,
    COMPLETE_PANEL_ASSIGNMENT_STATUS,
)
from .judge_round_commitment import JudgeRoundCommitment
from .judging_form_element import JudgingFormElement
from accelerator_abstract.models.base_judging_form_element import (
    FEEDBACK_ERROR,
    FEEDBACK_QUESTION,
    FORM_ELEM_COMPETITORS,
    FORM_ELEM_CUSTOMER_ACQUISITION,
    FORM_ELEM_CUSTOMER_PAIN_SOLUTION,
    FORM_ELEM_FINANCIALS,
    FORM_ELEM_OVERALL_IMPACT,
    FORM_ELEM_OVERALL_RECOMMENDATION,
    FORM_ELEM_REGULATION_IP,
    FORM_ELEM_TEAM,
    JUDGE_FEEDBACK_FORM_ELEMENTS,
    RECOMMENDATION_ERROR,
    RECOMMENDATION_QUESTION,
    FORM_ELEM_FEEDBACK_TO_STARTUP,
    FORM_ELEM_FEEDBACK_TO_MC,
)
from .judging_round import JudgingRound
from accelerator_abstract.models.base_judging_round import (
    CAPTURE_AVAILABILITY_DISABLED,
    CAPTURE_AVAILABILITY_TIME,
    DEFAULT_BUFFER_BEFORE_EVENT,
    FEEDBACK_DISPLAY_DISABLED,
    IN_PERSON_JUDGING_ROUND_TYPE,
    ONLINE_JUDGING_ROUND_TYPE,
    RECRUIT_NONE,
    RECRUIT_DISPLAY_ONLY,
    RECRUIT_ANYONE,
    RECRUIT_APPROVED_ONLY,
    FEEDBACK_DISPLAY_DISABLED,
    FEEDBACK_DISPLAY_ENABLED,
)

from .scenario import Scenario
from accelerator_abstract.models.base_scenario import DEFAULT_PANEL_SIZE
from .scenario_preference import ScenarioPreference
from accelerator_abstract.models.base_scenario_preference import (
    ALL_JUDGES,
    APPLICATION_ENTITY,
    ENTITY_TYPES,
    INDUSTRY_JUDGE_CATEGORIES,
    JUDGE_ALSO_KNOWS_INDUSTRY,
    JUDGE_CATEGORIES,
    JUDGE_ENTITY,
    JUDGE_GROUP_1,
    JUDGE_GROUP_2,
    JUDGE_GROUP_3,
    JUDGE_GROUP_4,
    JUDGE_GROUP_5,
    JUDGE_IN_INDUSTRY,
    JUDGE_IN_PROGRAM,
    JUDGE_IS_EXECUTIVE,
    JUDGE_IS_FEMALE,
    JUDGE_IS_INVESTOR,
    JUDGE_IS_LAWYER,
    JUDGE_IS_UNASSIGNED,
    JUDGE_KINDA_RELIABLE,
    JUDGE_MOST_RELIABLE,
    JUDGE_NOT_RELIABLE,
    JUDGE_OUTSIDE_PROGRAM,
    MAX_PREFERENCE,
    MIN_PREFERENCE,
    PREFERENCE_CONSTRAINT_TYPES,
    PROGRAM_JUDGE_CATEGORIES,
    SIMPLE_JUDGE_CATEGORIES,
    SPECIAL_JUDGE_CATEGORIES,
)
from .scenario_application import ScenarioApplication
from .scenario_judge import ScenarioJudge
from .mentoring_specialties import MentoringSpecialties
from .panel import Panel
from accelerator_abstract.models.base_panel import (
    ACTIVE_PANEL_STATUS,
    COMPLETED_PANEL_STATUS,
    DEFAULT_PANEL_STATUS,
    PANEL_STATUS_ENUM,
    PREVIEW_PANEL_STATUS,
)
from .judge_feedback_component import JudgeFeedbackComponent
from accelerator_abstract.models.base_judge_feedback_component import (
    DEFINITELY_DONT_RECOMMEND,
    DEFINITELY_RECOMMEND,
    DONT_RECOMMEND,
    JUDGE_FEEDBACK_REVIEWER,
    JUDGE_FEEDBACK_SANITIZER,
    LINEAR_SCORES,
    RECOMMEND,
    STRONGLY_DONT_RECOMMEND,
    STRONGLY_RECOMMEND,
    WEIGHTED_SCORES,
)

from .panel_location import PanelLocation
from .panel_time import PanelTime
from .panel_type import PanelType
from .application_panel_assignment import ApplicationPanelAssignment

from .paypal_payment import PayPalPayment
from .paypal_refund import PayPalRefund
from .startup_label import StartupLabel
from .user_label import UserLabel
from accelerator_abstract.models.base_user_label import (
    CONFIRMED_JUDGE_STATE,
    DESIRED_JUDGE_STATE,
    JUDGING_ROUND_FORMAT,
)
from .bucket_state import BucketState
from accelerator_abstract.models.base_bucket_state import (
    BaseBucketState,
    BUCKET_TYPES,
    FRESH_LEADS_GROUP,
    NEW_ENTREPRENEURS_BUCKET_TYPE,
    STALE_LEADS_GROUP,
    STALE_NOSTARTUP_BUCKET_TYPE,
    STALE_STARTUP_BUCKET_TYPE,
    SUBMITTED_BUCKET_TYPE,
    UNPAID_BUCKET_TYPE,
    UNSUBMITTED_BUCKET_TYPE,
)
from .file_page import FilePage
from .category_header_page import CategoryHeaderPage
from .core_profile import CoreProfile
from .node_published_for import NodePublishedFor
from .subnav_association import NodeSubNavAssociation
from .site_redirect_page import SiteRedirectPage
from .legal_check import LegalCheck
from .user_legal_check import UserLegalCheck

from .nav_tree import NavTree
from accelerator_abstract.models.base_nav_tree import (
    MC_SIDE_NAV_TREE_ALIAS,
)
from .nav_tree_item import NavTreeItem
