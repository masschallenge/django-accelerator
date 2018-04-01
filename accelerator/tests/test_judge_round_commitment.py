# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import JudgeRoundCommitmentFactory


class TestJudgeRoundCommitment(TestCase):

    def test_str(self):
        obj = JudgeRoundCommitmentFactory()
        name = str(obj)
        assert str(obj.judge) in name
        assert str(obj.judging_round) in name
