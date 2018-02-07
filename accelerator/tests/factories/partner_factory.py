import swapper
from factory import (
    DjangoModelFactory,
    Sequence,
    SubFactory,
)

from accelerator.apps import AcceleratorConfig

Partner = swapper.load_model(AcceleratorConfig.name, 'Partner')

from accelerator.tests.factories.organization_factory import OrganizationFactory


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
