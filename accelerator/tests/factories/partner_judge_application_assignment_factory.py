# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

import swapper
from factory import SubFactory
from factory.django import DjangoModelFactory
from accelerator.tests.factories import (
    ApplicationFactory,
    JudgingRoundFactory,
    PartnerFactory,
    UserFactory,
)
from accelerator.models import PartnerJudgeApplicationAssignment


class PartnerJudgeApplicationAssignment(DjangoModelFactory):
    judge = SubFactory(UserFactory)
    application = SubFactory(ApplicationFactory)
    judging_round = SubFactory(JudgingRoundFactory)
    partner = SubFactory(PartnerFactory)

    class Meta:
        model = PartnerJudgeApplicationAssignment
