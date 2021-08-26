# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from factory import (
    Sequence,
    SubFactory,
)
from factory.django import DjangoModelFactory

from accelerator.models import PartnerJudgingRoundChallenge
from accelerator.tests.factories import (
    JudgingRoundFactory,
    PartnerFactory,
)


class PartnerJudgingRoundChallengeFactory(DjangoModelFactory):
    class Meta:
        model = PartnerJudgingRoundChallenge

    judging_round = SubFactory(JudgingRoundFactory)
    partner = SubFactory(PartnerFactory)
    text = Sequence(lambda n: "partner judging round challenge text {}".format(n))
