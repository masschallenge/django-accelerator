# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from accelerator_abstract.models.accelerator_model import (
    AcceleratorModel,
    CHOICE_OPTION_HELP_TEXT
)
from accelerator_abstract.models.base_application_question import (
    CHOICE_LAYOUTS,
    TEXT_LIMIT_UNITS,
)

APPLICATION_ANSWER_DB_VALUE = 'answer'
APPLICATION_ANSWER_DISPLAY = 'Application Answer'
BOILERPLATE_DB_VALUE = 'boilerplate'
BOILERPLATE_DISPLAY = 'Boilerplate'
FEEDBACK_DB_VALUE = 'feedback'
FEEDBACK_DISPLAY = 'Feedback'

ELEMENT_TYPES = ((APPLICATION_ANSWER_DB_VALUE, APPLICATION_ANSWER_DISPLAY),
                 (BOILERPLATE_DB_VALUE, BOILERPLATE_DISPLAY),
                 (FEEDBACK_DB_VALUE, FEEDBACK_DISPLAY))
MULTILINE_DB_VALUE = 'multiline'
MULTILINE_DISPLAY = 'MultilineText'
MULTIPLE_CHOICE_DB_VALUE = 'multichoice'
MULTIPLE_CHOICE_DISPLAY = 'MultipleChoice'
NUMBER_DB_VALUE = 'number'
NUMBER_DISPLAY = 'Number'

FEEDBACK_TYPES = ((MULTILINE_DB_VALUE, MULTILINE_DISPLAY),
                  (MULTIPLE_CHOICE_DB_VALUE, MULTIPLE_CHOICE_DISPLAY),
                  (NUMBER_DB_VALUE, NUMBER_DISPLAY))
DASHBOARD_DISPLAY_VALUES = (('omit', 'Omit'),
                            ('value', 'Value'),
                            ('yesno', 'Yes/No'))
SHARE_WITH_STARTUP_DB_VALUE = 'share-with-startup'
SHARE_WITH_STARTUP_DISPLAY = 'Share with Startup'
ADMINISTRATOR_ONLY_DB_VALUE = 'administrator-only'
ADMINISTRATOR_ONLY_DISPLAY = 'Share with Program Administrators'
SHARING_VALUES = (
    (SHARE_WITH_STARTUP_DB_VALUE, SHARE_WITH_STARTUP_DISPLAY),
    (ADMINISTRATOR_ONLY_DB_VALUE, ADMINISTRATOR_ONLY_DISPLAY),
)
JUDGING_FORM_ELEMENT_UNICODE_TEMPLATE = "Element %s (%s) from the %s"
FORM_ELEM_OVERALL_RECOMMENDATION = "OVERALL_RECOMMENDATION"

FORM_ELEM_CUSTOMER_PAIN_SOLUTION = "CUSTOMER_PAIN_SOLUTION"
FORM_ELEM_OVERALL_IMPACT = "OVERALL_IMPACT"
FORM_ELEM_CUSTOMER_ACQUISITION = "CUSTOMER_ACQUISITION"
FORM_ELEM_COMPETITORS = "COMPETITORS"
FORM_ELEM_FINANCIALS = "FINANCIALS"
FORM_ELEM_REGULATION_IP = "REGULATION_IP"
FORM_ELEM_TEAM = "TEAM"

JUDGE_FEEDBACK_FORM_ELEMENTS = (
    FORM_ELEM_CUSTOMER_PAIN_SOLUTION,
    FORM_ELEM_OVERALL_IMPACT,
    FORM_ELEM_CUSTOMER_ACQUISITION,
    FORM_ELEM_COMPETITORS,
    FORM_ELEM_FINANCIALS,
    FORM_ELEM_REGULATION_IP,
    FORM_ELEM_TEAM,
)

FEEDBACK_QUESTION = "Written Feedback to the Startup"
FEEDBACK_ERROR = "JudgingFormElement for written feedback not found"
RECOMMENDATION_QUESTION = "Your Overall Recommendation"
RECOMMENDATION_ERROR = "JudgingFormElement for recommendation not found"

FORM_ELEM_FEEDBACK_TO_STARTUP = "FEEDBACK_TO_STARTUP"
FORM_ELEM_FEEDBACK_TO_MC = 'FEEDBACK_TO_MC'


@python_2_unicode_compatible
class BaseJudgingFormElement(AcceleratorModel):
    form_type = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "JudgingForm"),
        on_delete=models.CASCADE)
    element_number = models.IntegerField()
    element_name = models.CharField(max_length=50, blank=True)
    dashboard_label = models.CharField(max_length=50, blank=True)
    section_heading = models.CharField(max_length=40, blank=True)
    question_text = models.CharField(max_length=200, blank=True)
    help_text = models.CharField(max_length=1000, blank=True)
    element_type = models.CharField(
        max_length=64,
        choices=ELEMENT_TYPES,
    )
    feedback_type = models.CharField(
        max_length=64,
        choices=FEEDBACK_TYPES,
        blank=True,
    )
    display_value = models.CharField(
        max_length=64,
        choices=DASHBOARD_DISPLAY_VALUES,
    )
    score_element = models.BooleanField(default=False)
    mandatory = models.BooleanField(default=False)
    text_box_lines = models.IntegerField(null=True,
                                         default=0,
                                         blank=True)
    text_limit = models.IntegerField(null=True,
                                     default=0,
                                     blank=True)
    text_limit_units = models.CharField(
        max_length=64,
        choices=TEXT_LIMIT_UNITS,
        blank=True,
    )
    text_minimum = models.IntegerField(null=True,
                                       default=0,
                                       blank=True)
    text_minimum_units = models.CharField(
        max_length=64,
        choices=TEXT_LIMIT_UNITS,
        blank=True,
    )
    choice_options = models.CharField(
        max_length=200,
        blank=True,
        help_text=CHOICE_OPTION_HELP_TEXT
    )
    choice_layout = models.CharField(
        max_length=64,
        choices=CHOICE_LAYOUTS,
        blank=True,
    )
    application_question = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               "ApplicationQuestion"),
        blank=True,
        null=True,
        on_delete=models.CASCADE)
    sharing = models.CharField(
        max_length=64,
        choices=SHARING_VALUES,
        blank=True,
    )

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_judgingformelement'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True
        ordering = ['form_type', 'element_number', ]
        verbose_name_plural = 'Judging Form Elements'

    def __str__(self):
        return JUDGING_FORM_ELEMENT_UNICODE_TEMPLATE % (
            self.element_number, self.element_name, self.form_type.name)

    def parsed_choices(self):
        return self.choice_options.split('|')
