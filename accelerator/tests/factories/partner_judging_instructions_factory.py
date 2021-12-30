from __future__ import unicode_literals

from factory import (
    Sequence,
    SubFactory,
)
from factory.django import DjangoModelFactory


from accelerator.tests.factories.partner_factory import PartnerFactory
from accelerator.tests.factories.judging_round_factory import (
    JudgingRoundFactory
)

from accelerator.models import PartnerJudgingInstructions


class PartnerJudgingInstructionsFactory(DjangoModelFactory):
    class Meta:
        model = PartnerJudgingInstructions

    partner = SubFactory(PartnerFactory)
    judging_round = SubFactory(JudgingRoundFactory)
    instructions = Sequence(lambda n: "Instructions of Partner {0}".format(n))
