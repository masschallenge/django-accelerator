from __future__ import unicode_literals

import swapper
from factory import (
    Sequence,
    SubFactory,
)
from factory.django import DjangoModelFactory

from accelerator.tests.factories.program_factory import ProgramFactory

ProgramStartupAttribute = swapper.load_model('accelerator',
                                             'ProgramStartupAttribute')


class ProgramStartupAttributeFactory(DjangoModelFactory):
    class Meta:
        model = ProgramStartupAttribute

    program = SubFactory(ProgramFactory)
    attribute_type = "django.forms.CharField"
    attribute_label = Sequence(lambda n: "Attribute Label {0}".format(n))
    attribute_description = Sequence(lambda n: "Description {0}".format(n))
    admin_viewable = False
    non_admin_viewable = False
    staff_viewable = False
    finalist_viewable = False
    mentor_viewable = False
