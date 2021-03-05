# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import (
    Sequence,
    SubFactory,
)
from factory.django import DjangoModelFactory

from accelerator.tests.factories.application_factory import ApplicationFactory
from accelerator.tests.factories.panel_factory import PanelFactory
from accelerator.tests.factories.scenario_factory import ScenarioFactory

ApplicationPanelAssignment = swapper.load_model('accelerator',
                                                'ApplicationPanelAssignment')


class ApplicationPanelAssignmentFactory(DjangoModelFactory):
    class Meta:
        model = ApplicationPanelAssignment

    application = SubFactory(ApplicationFactory)
    panel = SubFactory(PanelFactory)
    scenario = SubFactory(ScenarioFactory)
    panel_slot_number = Sequence(lambda n: n)
    remote_pitch = False
    notes = "test assignment"
