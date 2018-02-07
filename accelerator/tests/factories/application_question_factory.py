# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from factory import (
    DjangoModelFactory,
    Sequence,
    SubFactory,
)

from accelerator.models.application_question import ApplicationQuestion
from accelerator.tests.factories.application_type_factory import ApplicationTypeFactory
from accelerator.tests.factories.question_factory import QuestionFactory


class ApplicationQuestionFactory(DjangoModelFactory):
    class Meta:
        model = ApplicationQuestion

    application_type = SubFactory(ApplicationTypeFactory)
    program = None
    question_number = Sequence(lambda n: n)
    section_heading = ""
    question_text = Sequence(lambda n: "Application Question {0}".format(n))
    help_text = ""
    mandatory = False
    text_box_lines = 10
    text_limit = 200
    text_limit_units = "characters"
    question = SubFactory(QuestionFactory)
