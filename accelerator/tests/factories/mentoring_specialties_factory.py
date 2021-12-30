from __future__ import unicode_literals

import swapper
from factory import Sequence
from factory.django import DjangoModelFactory

MentoringSpecialties = swapper.load_model('accelerator',
                                          'MentoringSpecialties')


class MentoringSpecialtiesFactory(DjangoModelFactory):
    class Meta:
        model = MentoringSpecialties

    name = Sequence(lambda n: "Mentoring Specialties {0}".format(n))
