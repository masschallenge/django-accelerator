# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import ScenarioPreferenceFactory


class TestScenarioPreference(TestCase):

    def test_str(self):
        scenario_preference = ScenarioPreferenceFactory()
        assert scenario_preference.constraint_type.lower() in str(
            scenario_preference)
        assert scenario_preference.entity_type.lower() in str(
            scenario_preference)
        assert scenario_preference.entity_set.lower() in str(
            scenario_preference)
