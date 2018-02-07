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
    email_domain = Sequence(lambda n: "pf{0}.masschallenge.org".format(n))
    phone_number = "617-555-1212"
    physical_address = "Boston"
