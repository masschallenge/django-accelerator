from factory import (
    Sequence,
)
from factory.django import DjangoModelFactory
from simpleuser.tests.factories.user_factory import UserFactory
from accelerator.tests.factories import OrganizationFactory
from accelerator.models import IndustryCluster


class IndustryClusterFactory(DjangoModelFactory):
    class Meta:
        model = IndustryCluster

    name = Sequence(lambda n: "Climate Cluster {0}".format(n))
    description = Sequence(
        lambda n: "Program interested in Climate {0}".format(n))
    image = None
