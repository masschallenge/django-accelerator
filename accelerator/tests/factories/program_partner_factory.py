# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import (
    DjangoModelFactory,
    Sequence,
    SubFactory,
)

from accelerator.apps import AcceleratorConfig
from accelerator.tests.factories.partner_factory import PartnerFactory
from accelerator.tests.factories.program_factory import ProgramFactory
from accelerator.tests.factories.program_partner_type_factory import (
    ProgramPartnerTypeFactory
)

ProgramPartner = swapper.load_model(AcceleratorConfig.name, 'ProgramPartner')


class ProgramPartnerFactory(DjangoModelFactory):
    class Meta:
        model = ProgramPartner

    program = SubFactory(ProgramFactory)
    partner = SubFactory(PartnerFactory)
    partner_type = SubFactory(ProgramPartnerTypeFactory)
    description = Sequence(
        lambda n: "Description of Program Partner #{0}".format(n))
