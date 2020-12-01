import swapper

from factory import fuzzy
from factory.django import DjangoModelFactory

from accelerator_abstract.models.base_ethno_racial_identity import (
    ETHNO_RACIAL_IDENTITY_CHOICES,
)

EthnoRacialIdentity = swapper.load_model('accelerator', 'EthnoRacialIdentity')

ETHNO_RACIAL_IDENTITY = [
    identity[0] for identity in ETHNO_RACIAL_IDENTITY_CHOICES
]


class EthnoRacialIdentityFactory(DjangoModelFactory):
    identity = fuzzy.FuzzyChoice(ETHNO_RACIAL_IDENTITY)

    class Meta:
        model = EthnoRacialIdentity
