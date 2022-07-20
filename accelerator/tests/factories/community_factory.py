from factory import Sequence
from factory.django import DjangoModelFactory

from accelerator.models import Community


class CommunityFactory(DjangoModelFactory):
    class Meta:
        model = Community
    name = Sequence(lambda n: "name {0}".format(n))
    email = Sequence(lambda n: "user_{0}@example.com".format(n))
    icon = "icon.jpg"
    image = "image.jpg"
    assignment_order = 2
