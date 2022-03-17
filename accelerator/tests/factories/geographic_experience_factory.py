from factory import Sequence
from factory.django import DjangoModelFactory

from accelerator.models.geographic_experience import (
    GeographicExperience
)


class GeographicExperienceFactory(DjangoModelFactory):
    class Meta:
        model = GeographicExperience

    name = Sequence(lambda n: "name {0}".format(n))
