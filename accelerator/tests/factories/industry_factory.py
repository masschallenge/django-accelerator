from __future__ import unicode_literals

import swapper
from factory import Sequence
from factory.django import DjangoModelFactory

Industry = swapper.load_model('accelerator', 'Industry')


class IndustryFactory(DjangoModelFactory):
    class Meta:
        model = Industry

    name = Sequence(lambda n: "Industry {0}".format(n))
    icon = Sequence(lambda n: "path_to_icon_{0}".format(n))

    # DO NOT provide a slot for parent.  The parent slot appears to get
    # handled correctly by MPTT and if you try to override
    # it, then you end up having to move a node between trees
    # which apparent MPTT does not support.
