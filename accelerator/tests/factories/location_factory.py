import swapper
from factory import (
    DjangoModelFactory,
    Sequence,
)

from accelerator.apps import AcceleratorConfig

Location = swapper.load_model(AcceleratorConfig.name, 'Location')


class LocationFactory(DjangoModelFactory):
    class Meta:
        model = Location

    name = Sequence(lambda n: "Location {0}".format(n))
    city = "Boston"
    state = "Massachusetts"
    country = "United States"
    postcode = "02210"
    latitude = "100"
    longitude = "200"
    timezone = "America/New_York"
