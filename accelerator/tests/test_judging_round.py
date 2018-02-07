# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import JudgingRoundFactory


class TestJudgingRound(TestCase):
    def test_str(self):
        judging_round = JudgingRoundFactory()
        assert judging_round.name in str(judging_round)
