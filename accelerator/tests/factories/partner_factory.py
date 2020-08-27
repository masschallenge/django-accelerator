# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import (
    Sequence,
    SubFactory,
)
from factory.django import DjangoModelFactory

from accelerator.apps import AcceleratorConfig
from accelerator.tests.factories.organization_factory import (
    OrganizationFactory
)

Partner = swapper.load_model(AcceleratorConfig.name, 'Partner')


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
