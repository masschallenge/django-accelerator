from factory import (
    Sequence,
    SubFactory,
)
from factory.django import DjangoModelFactory
from simpleuser.tests.factories.user_factory import UserFactory
from accelerator.tests.factories import OrganizationFactory
from accelerator.models import OrganizationNote


class OrganizationNoteFactory(DjangoModelFactory):
    class Meta:
        model = OrganizationNote

    organization = SubFactory(OrganizationFactory)
    author = SubFactory(UserFactory)
    note_content = Sequence(lambda n: "Organization note {0}".format(n))
