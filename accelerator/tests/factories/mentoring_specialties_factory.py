import swapper
from factory import (
    DjangoModelFactory,
    Sequence,
)

from accelerator.apps import AcceleratorConfig

MentoringSpecialties = swapper.load_model(AcceleratorConfig.name,
                                          'MentoringSpecialties')


class MentoringSpecialtiesFactory(DjangoModelFactory):
    class Meta:
        model = MentoringSpecialties

    name = Sequence(lambda n: "Mentoring Specialties {0}".format(n))
