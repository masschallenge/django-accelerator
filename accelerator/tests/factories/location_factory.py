import swapper
from factory import (
    DjangoModelFactory,
    Iterator,
    Sequence,
)

from accelerator.apps import AcceleratorConfig

Location = swapper.load_model(AcceleratorConfig.name, 'Location')


class LocationFactory(DjangoModelFactory):
    class Meta:
        model = Location

    name = Sequence(lambda n: "Location {0}".format(n))
    city = Sequence(lambda n: "city {0}".format(n))
    state = Sequence(lambda n: "state {0}".format(n))
    country = Sequence(lambda n: "country {0}".format(n))
    postcode = "00000"
    latitude = "11111"
    longitude = "22222"
    timezone = Iterator([
        "Africa/Kampala",
        "America/Argentina/Buenos_Aires",
        "America/Phoenix",
        "Asia/Bangkok",
        "Australia/Sydney"
    ])
