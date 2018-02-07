import swapper
from factory import (
    DjangoModelFactory,
    Sequence,
)

from accelerator.apps import AcceleratorConfig

Site = swapper.load_model(AcceleratorConfig.name, 'Site')


class SiteFactory(DjangoModelFactory):
    class Meta:
        model = Site

    name = Sequence(lambda n: "sitefactory{0}".format(n))
    security_key = Sequence(lambda n: (str(n) * 100 + '0')[0:100])
    description = "A Marketing site used for testing"
    site_url = Sequence(lambda n: "sitefactory{0}.com".format(n))
