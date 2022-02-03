from __future__ import unicode_literals

from datetime import (
    datetime,
    timedelta,
)

from factory import (
    Sequence,
    SubFactory,
    post_generation,
)
from factory.django import DjangoModelFactory

from pytz import utc

from accelerator.models.core_profile import CoreProfile
from accelerator.tests.factories.program_factory import ProgramFactory
from simpleuser.tests.factories.user_factory import UserFactory
from accelerator.tests.factories.location_factory import LocationFactory

class CoreProfileFactory(DjangoModelFactory):
    class Meta:
        model = CoreProfile
        abstract = True

    user = SubFactory(UserFactory)
    users_last_activity = utc.localize(datetime.now() + timedelta(-1))
    gender_self_description = ""
    phone = "+1-555-555-5555"
    linked_in_url = Sequence(lambda n: "http://www.linkedin.com/{0}".format(n))
    facebook_url = Sequence(lambda n: "http://www.facebook.com/{0}".format(n))
    twitter_handle = Sequence(lambda n: "tw{0}".format(n))
    personal_website_url = Sequence(
        lambda n: "http://example.com/{0}".format(n))
    landing_page = ""
    image = ""
    drupal_id = 0
    drupal_creation_date = None
    drupal_last_login = None
    current_program = SubFactory(ProgramFactory)
    newsletter_sender = False
    birth_year = None
    authorization_to_share_ethno_racial_identity = False
    user_location = SubFactory(LocationFactory)

    @post_generation
    def program_families(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for tag in extracted:
                self.program_families.add(tag)

    @post_generation
    def interest_categories(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for tag in extracted:
                self.interest_categories.add(tag)

    @post_generation
    def gender_identity(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for gender_choice in extracted:
                self.gender_identity.add(gender_choice)

    @post_generation
    def ethno_racial_identification(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for tag in extracted:
                self.ethno_racial_identification.add(tag)
