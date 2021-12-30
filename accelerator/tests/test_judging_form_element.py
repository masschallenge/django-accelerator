from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import JudgingFormElementFactory


class TestJudgingFormElement(TestCase):

    def test_str(self):
        jfe = JudgingFormElementFactory()
        assert str(jfe.element_number) in str(jfe)
        assert str(jfe.element_name) in str(jfe)
        assert str(jfe.form_type.name) in str(jfe)

    def test_parsed_choices(self):
        jfe = JudgingFormElementFactory(choice_options='a|b|c')
        choices = jfe.parsed_choices()
        assert isinstance(choices, list)
