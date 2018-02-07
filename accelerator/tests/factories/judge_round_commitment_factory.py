# -*- coding: utf-8 -*-

import swapper
from factory import (
    DjangoModelFactory,
    SubFactory,
)

from accelerator.apps import AcceleratorConfig

JudgeRoundCommitment = swapper.load_model(AcceleratorConfig.name,
                                          'JudgeRoundCommitment')

from accelerator.tests.factories.expert_factory import ExpertFactory
from accelerator.tests.factories.judging_round_factory import JudgingRoundFactory


class JudgeRoundCommitmentFactory(DjangoModelFactory):
    class Meta:
        model = JudgeRoundCommitment

    judge = SubFactory(ExpertFactory)
    judging_round = SubFactory(JudgingRoundFactory)
    commitment_state = True
    capacity = 10
    current_quota = 10
