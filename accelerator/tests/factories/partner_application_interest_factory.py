from accelerator.models import PartnerApplicationInterest
from factory import SubFactory
from factory.django import DjangoModelFactory
from accelerator.tests.factories import (
    ApplicationFactory,
    JudgingRoundFactory,
    PartnerFactory,
)

class PartnerApplicationInterestFactory(DjangoModelFactory):
    partner = SubFactory(PartnerFactory)
    application = SubFactory(ApplicationFactory)
    judging_round = SubFactory(JudgingRoundFactory)

    class Meta:
        model = PartnerApplicationInterest
