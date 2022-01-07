from __future__ import unicode_literals

import swapper
from factory import (
    Sequence,
    SubFactory,
)
from factory.django import DjangoModelFactory

from accelerator.tests.factories.entrepreneur_factory import (
    EntrepreneurFactory
)
from accelerator.tests.factories.startup_factory import StartupFactory

StartupTeamMember = swapper.load_model('accelerator', 'StartupTeamMember')


class StartupTeamMemberFactory(DjangoModelFactory):
    class Meta:
        model = StartupTeamMember

    startup = SubFactory(StartupFactory)
    user = SubFactory(EntrepreneurFactory)
    title = Sequence(lambda n: "Title {0}".format(n))
    startup_administrator = False
    primary_contact = False
    technical_contact = False
    marketing_contact = False
    financial_contact = False
    legal_contact = False
    product_contact = False
    design_contact = False
    display_on_public_profile = False
    founder = False
