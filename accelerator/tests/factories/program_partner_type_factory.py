import swapper
from factory import (
    DjangoModelFactory,
    Sequence,
    SubFactory,
)

from accelerator.apps import AcceleratorConfig

ProgramPartnerType = swapper.load_model(AcceleratorConfig.name,
                                        'ProgramPartnerType')


class ProgramPartnerTypeFactory(DjangoModelFactory):
    class Meta:
        model = ProgramPartnerType

    partner_type = Sequence(lambda n: 'Test Partner Type %d' % n)
    program = SubFactory("mc.tests.factories_old.DefaultProgramFactory")
    description = Sequence(
        lambda n: "Description of Program Partner Type #{0}".format(n))
    feature_in_footer = False
    sort_order = 1
    badge_image = None
    badge_display = "NONE"
