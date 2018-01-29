# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from django.core.exceptions import ValidationError
from django.db.models import (
    BooleanField,
    CharField,
    DateTimeField,
    ForeignKey,
    IntegerField,
    TextField,
)
from django.utils.encoding import python_2_unicode_compatible

from accelerator_abstract.models.accelerator_model import AcceleratorModel

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

FEEDBACK_DISPLAY_ITEMS = (
    ('feedback-and-judge-category', 'Judge Category and Feedback'),
    ('feedback-only', 'Only Feedback'),
    ('judge-category-only', 'Only Judge Category'))

DEFAULT_BUFFER_BEFORE_EVENT = 30
FIFTEEN_MINUTES = 15
BUFFER_TIMES = tuple([(i * FIFTEEN_MINUTES, i * FIFTEEN_MINUTES)
                      for i in range(9)])
START_MUST_PRECEDE_END_ERROR = 'Start date must precede end date'


@python_2_unicode_compatible
def validate_capacity_options(value):
    '''validate that the option is a pipe-separated list of integer values
    '''
    if value:
        try:
            map(int, value.split('|'))
        except ValueError as e:
            provided = e.message.split(':')[-1].strip()
            raise ValidationError(
                '{} is not an integer value'.format(provided))


@python_2_unicode_compatible
class BaseJudgingRound(AcceleratorModel):
    program = ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, 'Program'))
    cycle_based_round = BooleanField(
        default=False,
        help_text='Include startups from all programs in this Program\'s cycle'
    )
    name = CharField(max_length=60)
    start_date_time = DateTimeField(blank=True, null=True)
    end_date_time = DateTimeField(blank=True, null=True)
    is_active = BooleanField(default=False)
    round_type = CharField(
        choices=JUDGING_ROUND_TYPE_ENUM,
        max_length=10)
    application_type = ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               'ApplicationType'),
        blank=True,
        null=True)
    buffer_before_event = IntegerField(
        choices=BUFFER_TIMES,
        default=30,
        help_text='Choose a time in increments of 15 minutes.')
    judging_form = ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, 'JudgingForm'),
        blank=True, null=True)
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
                  'another round')
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
        help_text='Label for Startups')
    desired_judge_label = ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, 'UserLabel'),
        blank=True,
        null=True,
        help_text='Label for Desired Judges',
        related_name='rounds_desired_for')
    confirmed_judge_label = ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, 'UserLabel'),
        blank=True,
        null=True,
        help_text='Label for Confirmed Judges',
        related_name='rounds_confirmed_for')

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_judginground'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True
        unique_together = ('program', 'name')
        ordering = ['program__program_status',
                    '-program__end_date',
                    '-end_date_time',
                    'name']
        verbose_name_plural = 'Judging Rounds'

    def __str__(self):
        return '%s in %s' % (self.name, self.program)
