# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from django.db.models import (
    BooleanField,
    CharField,
    DateTimeField,
    ForeignKey,
    IntegerField,
    TextField,
    CASCADE,
)

from accelerator_abstract.models.accelerator_model import AcceleratorModel
from accelerator_abstract.utils import validate_capacity_options

ONLINE_JUDGING_ROUND_TYPE = 'Online'
IN_PERSON_JUDGING_ROUND_TYPE = 'In-Person'

JUDGING_ROUND_TYPE_ENUM = (
    (ONLINE_JUDGING_ROUND_TYPE, ONLINE_JUDGING_ROUND_TYPE),
    (IN_PERSON_JUDGING_ROUND_TYPE, IN_PERSON_JUDGING_ROUND_TYPE),
)

RECRUIT_NONE = 'NO'
RECRUIT_ANYONE = 'ANYONE'
RECRUIT_APPROVED_ONLY = 'APPROVEDONLY'
RECRUIT_DISPLAY_ONLY = 'DISPLAYONLY'
RECRUIT_JUDGES_ENUM = (
    (RECRUIT_NONE, 'Do not recruit judges or display prior commitments'),
    (RECRUIT_ANYONE, 'Recruit any expert'),
    (RECRUIT_APPROVED_ONLY, 'Recruit only approved judges'),
    (RECRUIT_DISPLAY_ONLY, 'Only display judges prior commitments'))

CAPTURE_AVAILABILITY_DISABLED = 'disabled'
CAPTURE_AVAILABILITY_LOCATION = 'location-only'
CAPTURE_AVAILABILITY_TIME = 'time-only'
CAPTURE_AVAILABILITY_TIME_TYPE = 'time-type'
CAPTURE_AVAILABILITY_TIME_TYPE_LOC = 'time-type-location'
CAPTURE_AVAILABILITY_TYPE = 'type-only'
CAPTURE_AVAILABILITY_CHOICES = (
    (CAPTURE_AVAILABILITY_DISABLED, 'Disabled'),
    (CAPTURE_AVAILABILITY_LOCATION, 'Capture location only'),
    (CAPTURE_AVAILABILITY_TIME, 'Capture time only'),
    (CAPTURE_AVAILABILITY_TYPE, 'Capture type only'),
)
CAPTURE_AVAILABILITY_FIELDS = {
    CAPTURE_AVAILABILITY_LOCATION: 'panellocation_set',
    CAPTURE_AVAILABILITY_TIME: 'paneltime_set',
    CAPTURE_AVAILABILITY_TYPE: 'paneltype_set',
}
CAPTURE_AVAILABILITY_TEMPLATES = {
    CAPTURE_AVAILABILITY_LOCATION: '||%s',
    CAPTURE_AVAILABILITY_TIME: '%s||',
    CAPTURE_AVAILABILITY_TYPE: '|%s|'
}

FEEDBACK_DISPLAY_DISABLED = 'disabled'
FEEDBACK_DISPLAY_ENABLED = 'enabled'
FEEDBACK_DISPLAY_CHOICES = (
    (FEEDBACK_DISPLAY_DISABLED, 'Disabled'),
    (FEEDBACK_DISPLAY_ENABLED, 'Enabled'),
)
FEEDBACK_DISPLAY_CATEGORY_AND_FEEDBACK = 'feedback-and-judge-category'
FEEDBACK_DISPLAY_CATEGORY_AND_FEEDBACK_TEXT = 'Judge Category and Feedback'
FEEDBACK_DISPLAY_FEEDBACK_ONLY = 'feedback-only'
FEEDBACK_DISPLAY_FEEDBACK_ONLY_TEXT = 'Only Feedback'
FEEDBACK_DISPLAY_CATEGORY_ONLY = 'judge-category-only'
FEEDBACK_DISPLAY_CATEGORY_ONLY_TEXT = 'Only Judge Category'

FEEDBACK_DISPLAY_ITEMS = (
    (FEEDBACK_DISPLAY_CATEGORY_AND_FEEDBACK,
     FEEDBACK_DISPLAY_CATEGORY_AND_FEEDBACK_TEXT),
    (FEEDBACK_DISPLAY_FEEDBACK_ONLY,
     FEEDBACK_DISPLAY_FEEDBACK_ONLY_TEXT),
    (FEEDBACK_DISPLAY_CATEGORY_ONLY,
     FEEDBACK_DISPLAY_CATEGORY_ONLY_TEXT),
)

DEFAULT_BUFFER_BEFORE_EVENT = 30
FIFTEEN_MINUTES = 15
BUFFER_TIMES = tuple([(i * FIFTEEN_MINUTES, i * FIFTEEN_MINUTES)
                      for i in range(9)])
START_MUST_PRECEDE_END_ERROR = 'Start date must precede end date'

SCENARIO_DETECTION = 'scenario'
PANEL_TIME_DETECTION = 'panel_time'
PANEL_SLOT_DETECTION = 'panel_slot'
COLLISION_DETECTION_CHOICES = (
    (SCENARIO_DETECTION, "Check that applications are not added to a scenario"
        " twice"),
    (PANEL_TIME_DETECTION, "Check that applications are not added to the same"
        " panel time within active scenarios twice"),
    (PANEL_SLOT_DETECTION, "Check that applications are not added to the same"
        " panel time and slot within active scenarios twice")
)


class BaseJudgingRound(AcceleratorModel):
    program = ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, 'Program'),
        on_delete=CASCADE)
    cycle_based_round = BooleanField(
        default=False,
        help_text='Include startups from all programs in this Program\'s cycle'
    )
    name = CharField(max_length=60)
    start_date_time = DateTimeField(blank=False, null=False, default=None)
    end_date_time = DateTimeField(blank=False, null=False, default=None)
    is_active = BooleanField(default=False)
    round_type = CharField(
        choices=JUDGING_ROUND_TYPE_ENUM,
        max_length=10)
    allow_dynamic_allocation = BooleanField(
        default=False,
        help_text=("Check this button to allow judges to get new applications "
                   "without manual allocation by staff."))
    application_type = ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               'ApplicationType'),
        blank=True,
        null=True,
        on_delete=CASCADE)
    buffer_before_event = IntegerField(
        choices=BUFFER_TIMES,
        default=30,
        help_text='Choose a time in increments of 15 minutes.')
    judging_form = ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, 'JudgingForm'),
        blank=True, null=True, on_delete=CASCADE)
    recruit_judges = CharField(
        max_length=16,
        choices=RECRUIT_JUDGES_ENUM,
        default=RECRUIT_NONE)
    recruiting_prompt = TextField(
        blank=True,
        help_text='You may use HTML, including links')
    positive_recruiting_prompt = TextField(
        'Positive Recruiting Response Label',
        blank=True,
        help_text='You may use HTML, including links')
    negative_recruiting_prompt = TextField(
        'Negative Recruiting Response Label',
        blank=True,
        help_text='You may use HTML, including links')
    capture_capacity = BooleanField(default=False)
    capacity_prompt = TextField(
        blank=True,
        help_text='You may use HTML, including links')
    capacity_options = CharField(
        max_length=255,
        blank=True,
        help_text='Provide a list of integers, separated by \'|\' '
                  '(like 10|20|30)',
        validators=[validate_capacity_options], )
    capture_availability = CharField(
        max_length=32,
        choices=CAPTURE_AVAILABILITY_CHOICES,
        default=CAPTURE_AVAILABILITY_DISABLED)
    feedback_display = CharField(
        choices=FEEDBACK_DISPLAY_CHOICES,
        default=FEEDBACK_DISPLAY_DISABLED,
        max_length=10)
    feedback_merge_with = ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               'JudgingRound'),
        blank=True,
        null=True,
        help_text='Optional: merge the display of this feedback with '
                  'another round',
        on_delete=CASCADE)
    feedback_display_message = TextField(
        blank=True,
        help_text='You may use HTML, including links (not relevant if '
                  'merged with another round)')
    feedback_display_items = CharField(
        max_length=64,
        blank=True,
        choices=FEEDBACK_DISPLAY_ITEMS,
        help_text='Not relevant if merged with another round')
    judge_instructions = TextField(
        blank=True,
        help_text='Instructions to present to judges in this round on their '
                  'judging portal.')
    presentation_mins = IntegerField(
        blank=True,
        default=20,
        help_text='Duration of startup pitch to judges, in minutes')
    buffer_mins = IntegerField(
        blank=True,
        default=10,
        help_text='Time between startup pitches, in minutes')
    break_mins = IntegerField(
        blank=True,
        default=10,
        help_text='Duration of judges\' coffee break(s), in minutes')
    num_breaks = IntegerField(
        blank=True,
        default=1,
        help_text=('Number of breaks the judges will be given '
                   'during a judging panel'))
    startup_label = ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               'StartupLabel'),
        blank=True,
        null=True,
        help_text='Label for Startups',
        on_delete=CASCADE)
    desired_judge_label = ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, 'UserLabel'),
        blank=True,
        null=True,
        help_text='Label for Desired Judges',
        related_name='rounds_desired_for',
        on_delete=CASCADE)
    confirmed_judge_label = ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, 'UserLabel'),
        blank=True,
        null=True,
        help_text='Label for Confirmed Judges',
        related_name='rounds_confirmed_for',
        on_delete=CASCADE)
    collision_detection_mode = CharField(
        max_length=10,
        blank=False,
        default=SCENARIO_DETECTION,
        choices=COLLISION_DETECTION_CHOICES)
    champion_partner_label = ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, 'PartnerLabel'),
        blank=True,
        null=True,
        help_text='Partner Label',
        on_delete=CASCADE)

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_judginground'
        abstract = True
        unique_together = ('program', 'name')
        ordering = ['program__program_status',
                    '-program__end_date',
                    '-end_date_time',
                    'name']
        verbose_name_plural = 'Judging Rounds'

    def __str__(self):
        return '%s in %s' % (self.name, self.program)

    def short_name(self, program=None):
        return "{year_month} {family_abbrs} {round_name}".format(
            year_month=self.year_month(),
            family_abbrs=self.program_family_abbrs(program),
            round_name=self.name)

    def year_month(self):
        date = self.end_date_time
        return "{year}-{month:02}".format(year=date.year, month=date.month)

    def program_family_abbrs(self, program=None):
        if program:
            return program.family_abbr()
        if self.cycle_based_round:
            programs = self.program.cycle.programs.all()
            abbrs = map(lambda s: s.upper(),
                        programs.values_list("program_family__url_slug",
                                             flat=True))
            return " ".join(sorted(abbrs))
        return self.program.family_abbr()

    def display_name(self, program=None):
        _program = program or self.program
        return "{year}-{month:02} {family_abbr} {round_name}".format(
            year=self.end_date_time.year,
            month=self.end_date_time.month,
            family_abbr=_program.family_abbr(),
            round_name=self.name)
