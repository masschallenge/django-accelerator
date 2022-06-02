from __future__ import unicode_literals

import swapper
from factory import (
    Sequence,
    SubFactory,
    post_generation,
)
from factory.django import DjangoModelFactory

from accelerator.tests.factories.organization_factory import (
    OrganizationFactory
)
from accelerator.tests.factories.industry_factory import IndustryFactory

Partner = swapper.load_model('accelerator', 'Partner')


class PartnerFactory(DjangoModelFactory):
    class Meta:
        model = Partner

    organization = SubFactory(OrganizationFactory)
    description = Sequence(lambda n: "Description of Partner {0}".format(n))
    partner_logo = None
    website_url = Sequence(lambda n: "www.partner{0}.com".format(n))
    twitter_handle = Sequence(lambda n: "partner{0}".format(n))
    public_inquiry_email = Sequence(
        lambda n: "contact@partner{0}.com".format(n))
    primary_industry = SubFactory(IndustryFactory)
    short_pitch = name = Sequence(
        lambda n: "short_pitch Partner {0} Inc.".format(n))
    full_elevator_pitch = Sequence(
        lambda n: "full_elevator_pitch Partner {0} Inc.".format(n))
    video_elevator_pitch_url = ""
    linked_in_url = Sequence(lambda n: "linkedin.com/partner{0}".format(n))
    facebook_url = Sequence(lambda n: "facebook.com/partner{0}".format(n))
    location_national = "United States"
    location_regional = "Massachusetts"
    location_city = "Boston"
    location_street_address = "212 Mckinnon Rd"
    date_founded = "01/2022"


@post_generation
def additional_industries(self, create, extracted, **kwargs):
    if not create:
        return
    if extracted:
        for industry in extracted:
            self.additional_industries.add(industry)
