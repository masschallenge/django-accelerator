from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import JudgeFeedbackComponentFactory


class TestJudgeFeedbackComponent(TestCase):

    def test_str(self):
        jaf = JudgeFeedbackComponentFactory()
        assert str(jaf.feedback_element.element_number) in str(jaf)
        assert str(jaf.judge_feedback.judge) in str(jaf)
