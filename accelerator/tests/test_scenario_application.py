from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import ScenarioApplicationFactory


class TestScenarioApplication(TestCase):

    def test_str(self):
        scenario_application = ScenarioApplicationFactory()
        assert str(scenario_application.scenario) in str(scenario_application)
        assert str(scenario_application.application) in str(
            scenario_application)
