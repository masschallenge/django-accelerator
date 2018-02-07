# -*- coding: utf-8 -*-

import swapper
from factory import (
    DjangoModelFactory,
    Sequence,
    SubFactory,
)

from accelerator.apps import AcceleratorConfig
from accelerator.models import COMPLETE_PANEL_ASSIGNMENT_STATUS

JudgePanelAssignment = swapper.load_model(AcceleratorConfig.name,
                                          'JudgePanelAssignment')

from accelerator.tests.factories.expert_factory import ExpertFactory
from accelerator.tests.factories.panel_factory import PanelFactory
from accelerator.tests.factories.scenario_factory import ScenarioFactory


class JudgePanelAssignmentFactory(DjangoModelFactory):
    class Meta:
        model = JudgePanelAssignment

    judge = SubFactory(ExpertFactory)
    panel = SubFactory(PanelFactory)
    scenario = SubFactory(ScenarioFactory)
    assignment_status = COMPLETE_PANEL_ASSIGNMENT_STATUS
    panel_sequence_number = Sequence(lambda n: n)
