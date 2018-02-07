import swapper
from factory import (
    DjangoModelFactory,
    Sequence,
    SubFactory,
)

from accelerator.apps import AcceleratorConfig

ProgramPartner = swapper.load_model(AcceleratorConfig.name, 'ProgramPartner')

from .partner_factory import PartnerFactory
from .program_partner_type_factory import ProgramPartnerTypeFactory
from accelerator.tests.factories.program_factory import ProgramFactory


class ProgramPartnerFactory(DjangoModelFactory):
    class Meta:
        model = ProgramPartner

    program = SubFactory(ProgramFactory)
    partner = SubFactory(PartnerFactory)
    partner_type = SubFactory(ProgramPartnerTypeFactory)
    description = Sequence(
        lambda n: "Description of Program Partner #{0}".format(n))
