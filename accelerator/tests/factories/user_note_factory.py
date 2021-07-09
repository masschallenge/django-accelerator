from factory import (
    Sequence,
    SubFactory,
)
from factory.django import DjangoModelFactory
from simpleuser.tests.factories.user_factory import UserFactory
from accelerator.models import UserNote


class UserNoteFactory(DjangoModelFactory):
    class Meta:
        model = UserNote

    user = SubFactory(UserFactory)
    author = SubFactory(UserFactory)
    note_content = Sequence(lambda n: "User note {0}".format(n))
