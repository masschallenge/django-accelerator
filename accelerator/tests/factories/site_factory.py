from __future__ import unicode_literals

import swapper
from factory import Sequence
from factory.django import DjangoModelFactory

Site = swapper.load_model('accelerator', 'Site')


class SiteFactory(DjangoModelFactory):
    class Meta:
        model = Site

    name = Sequence(lambda n: "sitefactory{0}".format(n))
    security_key = Sequence(lambda n: (str(n) * 100 + '0')[0:100])
    description = "A Marketing site used for testing"
    site_url = Sequence(lambda n: "sitefactory{0}.com".format(n))
