import swapper

from factory import Sequence, SubFactory
    
from factory.django import DjangoModelFactory
from pytz import utc

from simpleuser.tests.factories.user_factory import UserFactory

Note = swapper.load_model('accelerator', 'Note')


class NoteFactory(DjangoModelFactory):
    class Meta:
        model = Note

    user = SubFactory(UserFactory)
    manager = SubFactory(UserFactory)
    note_content = Sequence(lambda n: "staff note {0}".format(n))
