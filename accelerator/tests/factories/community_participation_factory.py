from factory import Sequence
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice

from accelerator.models.community_participation import (
    PARTICIPATION_CHOICES,
    CommunityParticipation,
)


class CommunityParticipationFactory(DjangoModelFactory):
    class Meta:
        model = CommunityParticipation
    name = Sequence(lambda n: "name {0}".format(n))
    description = Sequence(lambda n: "description {0}".format(n))
    sort_order = Sequence(lambda n: n)
    type = FuzzyChoice([type[0] for type in PARTICIPATION_CHOICES])
