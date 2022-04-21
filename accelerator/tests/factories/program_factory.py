from __future__ import unicode_literals

from decimal import Decimal

import swapper
from factory import (
    Sequence,
    SubFactory,
    post_generation,
)
from factory.django import DjangoModelFactory

from accelerator.models import ACTIVE_PROGRAM_STATUS
from accelerator.tests.factories.program_cycle_factory import (
    ProgramCycleFactory
)
from accelerator.tests.factories.program_family_factory import (
    ProgramFamilyFactory
)
from accelerator.tests.utils import months_from_now

Program = swapper.load_model('accelerator', 'Program')


class ProgramFactory(DjangoModelFactory):
    class Meta:
        model = Program

    name = Sequence(lambda n: "Name of Program {0}".format(n))
    program_family = SubFactory(ProgramFamilyFactory)
    cycle = SubFactory(ProgramCycleFactory)
    description = Sequence(lambda n: "Description for Program {0}".format(n))
    start_date = months_from_now(-2)
    end_date = months_from_now(2)
    location = Sequence(
        lambda n: "Location Program {0}".format(n))
    program_status = ACTIVE_PROGRAM_STATUS
    currency_code = "USD"
    early_application_fee = Decimal(49.00)
    regular_application_fee = Decimal(99.00)
    regular_fee_suffix = ""
    interested_judge_message = Sequence(
        lambda n: "Interested Judge Program {0}".format(n))
    approved_judge_message = Sequence(
        lambda n: "Approved Judge Program {0}".format(n))
    interested_mentor_message = Sequence(
        lambda n: "Interested Mentor Program {0}".format(n))
    approved_mentor_message = Sequence(
        lambda n: "Approved Mentor Program {0}".format(n))
    interested_speaker_message = Sequence(
        lambda n: "Interested Speaker Program {0}".format(n))
    approved_speaker_message = Sequence(
        lambda n: "Approved Speaker Program {0}".format(n))
    interested_office_hours_message = Sequence(
        lambda n: "Interested Office Hours Program {0}".format(n))
    approved_office_hours_message = Sequence(
        lambda n: "Approved Office Hours Program {0}".format(n))
    refund_code_support = "enabled"
    many_codes_per_partner = False
    url_slug = Sequence(lambda n: "p{0}".format(n))
    overview_start_date = None
    overview_deadline_date = None
    mentor_program_group = None

    @post_generation
    def supported_innovation_stages(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for stage in extracted:
                self.supported_innovation_stages.add(stage)

    @post_generation
    def supported_industry_clusters(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for cluster in extracted:
                self.supported_industry_clusters.add(cluster)
