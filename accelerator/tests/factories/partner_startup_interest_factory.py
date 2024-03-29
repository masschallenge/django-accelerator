from __future__ import unicode_literals

from factory import SubFactory

from factory.django import DjangoModelFactory

from accelerator.models import PartnerJudgingRoundChallenge
from accelerator.tests.factories import (
    JudgingRoundFactory,
    PartnerFactory,
    StartupFactory,
)


class PartnerJudgingRoundChallengeFactory(DjangoModelFactory):
    class Meta:
        model = PartnerJudgingRoundChallenge

    judging_round = SubFactory(JudgingRoundFactory)
    partner = SubFactory(PartnerFactory)
    startup = SubFactory(StartupFactory)
    advance_to_next_round = False
