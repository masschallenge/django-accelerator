# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from factory import SubFactory
from factory.django import DjangoModelFactory


from accelerator.models import JudgeRoundCommitment
from accelerator.tests.factories.expert_factory import ExpertFactory
from accelerator.tests.factories.judging_round_factory import (
    JudgingRoundFactory
)


class JudgeRoundCommitmentFactory(DjangoModelFactory):
    class Meta:
        model = JudgeRoundCommitment

    judge = SubFactory(ExpertFactory)
    judging_round = SubFactory(JudgingRoundFactory)
    commitment_state = True
    capacity = 10
    current_quota = 10
