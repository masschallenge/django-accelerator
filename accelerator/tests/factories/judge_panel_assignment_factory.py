# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import (
    Sequence,
    SubFactory,
)
from factory.django import DjangoModelFactory

from accelerator.accelerator.models import COMPLETE_PANEL_ASSIGNMENT_STATUS
from accelerator.accelerator.tests.factories.expert_factory import ExpertFactory
from accelerator.accelerator.tests.factories.panel_factory import PanelFactory
from accelerator.accelerator.tests.factories.scenario_factory import ScenarioFactory

JudgePanelAssignment = swapper.load_model('accelerator',
                                          'JudgePanelAssignment')


class JudgePanelAssignmentFactory(DjangoModelFactory):
    class Meta:
        model = JudgePanelAssignment

    judge = SubFactory(ExpertFactory)
    panel = SubFactory(PanelFactory)
    scenario = SubFactory(ScenarioFactory)
    assignment_status = COMPLETE_PANEL_ASSIGNMENT_STATUS
    panel_sequence_number = Sequence(lambda n: n)
