# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper

from factory import (
    Sequence,
    SubFactory,
)
from factory.django import DjangoModelFactory


from accelerator.tests.factories.partner_factory import PartnerFactory
from accelerator.tests.factories.judging_round_factory import (
    JudgingRoundFactory
)

PartnerJudgingInstruction = swapper.load_model('accelerator',
                                          'PartnerJudgingInstruction')


class PartnerJudgingRoundFactory(DjangoModelFactory):
    class Meta:
        model = PartnerJudgingInstruction

    partner = SubFactory(PartnerFactory)
    judging_round = SubFactory(JudgingRoundFactory)
    instruction = Sequence(lambda n: "Instruction of Partner {0}".format(n))
