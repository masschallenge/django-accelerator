# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import ApplicationAnswerFactory


class TestApplicationAnswer(TestCase):

    def test_str(self):
        application_answer = ApplicationAnswerFactory()
        assert (application_answer.application.startup.name in
                application_answer.__str__())
        assert (str(application_answer.application_question.question_number) in
                application_answer.__str__())
