from __future__ import unicode_literals

import swapper
from factory import (
    Sequence,
    SubFactory,
)
from factory.django import DjangoModelFactory

from accelerator.tests.factories.application_question_factory import (
    ApplicationQuestionFactory
)
from accelerator.tests.factories.judging_form_factory import JudgingFormFactory

JudgingFormElement = swapper.load_model('accelerator',
                                        'JudgingFormElement')


class JudgingFormElementFactory(DjangoModelFactory):
    class Meta:
        model = JudgingFormElement

    form_type = SubFactory(JudgingFormFactory)
    element_number = Sequence(lambda n: n)
    element_name = Sequence(lambda n: "Judging Form Element {0}".format(n))
    dashboard_label = ""
    section_heading = ""
    question_text = Sequence(lambda n: "Judging Form Question {0}".format(n))
    help_text = ""
    element_type = "answer"
    feedback_type = ""
    display_value = "value"
    mandatory = False
    text_box_lines = 0
    text_limit = 0
    text_limit_units = ""
    text_minimum = 0
    text_minimum_units = ""
    choice_options = ""
    choice_layout = ""
    application_question = SubFactory(ApplicationQuestionFactory)
    sharing = ""
