# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import JudgeApplicationFeedbackFactory


class TestJudgeApplicationFeedback(TestCase):
    def test_str(self):
        jaf = JudgeApplicationFeedbackFactory()
        expected_str = jaf.STR_FORMAT % (jaf.application, jaf.judge)
        assert str(jaf) == expected_str
