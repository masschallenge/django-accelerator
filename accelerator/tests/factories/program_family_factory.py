# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import (
    DjangoModelFactory,
    Sequence,
)

from accelerator.apps import AcceleratorConfig

ProgramFamily = swapper.load_model(AcceleratorConfig.name, 'ProgramFamily')


class ProgramFamilyFactory(DjangoModelFactory):
    class Meta:
        model = ProgramFamily

    name = Sequence(lambda n: "Program Family {0}".format(n))
    short_description = 'A program family for testing'
    url_slug = Sequence(lambda n: "pf{0}".format(n))
    email_domain = Sequence(lambda n: "pf{0}.accelerator.org".format(n))
    phone_number = "617-555-1212"
    is_open_for_startups = True
    is_open_for_experts = True
    use_site_tree_side_nav = False
