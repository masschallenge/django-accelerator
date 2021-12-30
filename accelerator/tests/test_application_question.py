from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import (
    ApplicationQuestionFactory,
)


class TestApplicationQuestion(TestCase):
    def test_str(self):
        app_question = ApplicationQuestionFactory()
        expected_str = app_question.STR_FORMAT % (
            app_question.question_number,
            app_question.question_text[:10],
            app_question.application_type.name)
        assert str(app_question) == expected_str

    def test_parsed_choices(self):
        app_question = ApplicationQuestionFactory(choice_options='a|b|c')
        choices = app_question.parsed_choices()
        assert isinstance(choices, list)
