from __future__ import unicode_literals

import swapper
from factory import (
    Iterator,
    Sequence,
    SubFactory,
    post_generation,
)
from factory.django import DjangoModelFactory

from accelerator.models import (
    DEFAULT_PROFILE_BACKGROUND_COLOR,
    DEFAULT_PROFILE_TEXT_COLOR,
    STARTUP_COMMUNITIES,
)
from accelerator.tests.factories.currency_factory import CurrencyFactory
from accelerator.tests.factories.entrepreneur_factory import (
    EntrepreneurFactory
)
from accelerator.tests.factories.industry_factory import IndustryFactory
from accelerator.tests.factories.organization_factory import (
    OrganizationFactory
)
from accelerator.tests.utils import days_from_now

Startup = swapper.load_model('accelerator', 'Startup')

COMMUNITY_VALUES = [val[0] for val in STARTUP_COMMUNITIES]


class StartupFactory(DjangoModelFactory):
    class Meta:
        model = Startup

    organization = SubFactory(OrganizationFactory)
    user = SubFactory(EntrepreneurFactory)
    is_visible = True
    primary_industry = SubFactory(IndustryFactory)

    short_pitch = name = Sequence(
        lambda n: "short_pitch Startup {0} Inc.".format(n))
    full_elevator_pitch = Sequence(
        lambda n: "full_elevator_pitch Startup {0} Inc.".format(n))
    video_elevator_pitch_url = ""
    website_url = Sequence(lambda n: "startup{0}.com".format(n))
    linked_in_url = Sequence(lambda n: "linkedin.com/startup{0}".format(n))
    facebook_url = Sequence(lambda n: "facebook.com/startup{0}".format(n))
    high_resolution_logo = None
    twitter_handle = Sequence(lambda n: "startup{0}".format(n))
    public_inquiry_email = Sequence(
        lambda n: "contact@startup{0}.com".format(n))
    created_datetime = days_from_now(-5)
    last_updated_datetime = days_from_now(-4)
    community = Iterator(COMMUNITY_VALUES)
    profile_background_color = DEFAULT_PROFILE_BACKGROUND_COLOR
    profile_text_color = DEFAULT_PROFILE_TEXT_COLOR
    currency = SubFactory(CurrencyFactory)
    location_national = "United States"
    location_regional = "Massachusetts"
    location_city = "Boston"
    location_postcode = "02210"
    location_street_address = "212 Mckinnon Rd"
    date_founded = "01/2010"
    landing_page = None
    acknowledgement = True
    is_startup = False
    bipoc_founder = False
    female_or_transgender_founder = False
    first_time_founder = False

    @post_generation
    def additional_industries(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for industry in extracted:
                self.additional_industries.add(industry)

    @post_generation
    def name(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            self.organization.name = extracted
            self.organization.save()
