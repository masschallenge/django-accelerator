# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
import factory
from factory import (
    DjangoModelFactory,
    Sequence,
    SubFactory,
)

from accelerator.apps import AcceleratorConfig
from accelerator.tests.factories.entrepreneur_factory import (
    EntrepreneurFactory
)
from accelerator.tests.factories.startup_factory import StartupFactory
from mc.signals import (
    added_startup_team_member,
    delete_partner_member,
    edited_startup_profile,
    paypal_payment_refunded,
    refund_code_applied,
    refund_code_failed,
    removed_program_interest,
    removed_startup_team_member,
    saved_program_interest,
    startup_created,
    sync_startup_members,
    update_partner_member,
    user_attempted_payment,
    startup_team_member_role_unset,
    startup_team_member_role_set,
    user_failed_to_register_for_earlybird,
    user_successfully_registered_for_earlybird,
)
from django.db.models.signals import pre_save, post_save

StartupTeamMember = swapper.load_model(
    AcceleratorConfig.name,
    'StartupTeamMember')


@factory.django.mute_signals(pre_save, post_save)
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
