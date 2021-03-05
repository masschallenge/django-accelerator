# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import Sequence
from factory.django import DjangoModelFactory

Organization = swapper.load_model('accelerator', 'Organization')


class OrganizationFactory(DjangoModelFactory):
    class Meta:
        model = Organization

    name = Sequence(lambda n: "Test Organization {0}".format(n))
    website_url = Sequence(lambda n: "www.organization{0}.com".format(n))
    twitter_handle = Sequence(lambda n: "organization{0}".format(n))
    public_inquiry_email = Sequence(
        lambda n: "contact@organization{0}.com".format(n))
    url_slug = ""  # Allow this to get computed late
