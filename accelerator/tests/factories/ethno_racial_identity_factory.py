import swapper

from factory import Sequence
from factory.django import DjangoModelFactory

EthnoRacialIdentity = swapper.load_model('accelerator', 'EthnoRacialIdentity')


class EthnoRacialIdentityFactory(DjangoModelFactory):
    identity = Sequence(lambda n: "ethno racial identity {0}".format(n))

    class Meta:
        model = EthnoRacialIdentity
