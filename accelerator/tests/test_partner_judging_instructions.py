# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import PartnerJudgingInstructionsFactory


class TestPartnerJudgingInstructions(TestCase):
    def test_str(self):
        obj = PartnerJudgingInstructionsFactory()
        partner_judging_instruction = str(obj)
        assert str(obj.judging_round) in partner_judging_instruction
        assert str(obj.partner) in partner_judging_instruction
        assert str(obj.instructions) in partner_judging_instruction
