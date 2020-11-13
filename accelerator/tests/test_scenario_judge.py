# MIT License
# Copyright (c) 2017 MassChallenge, Inc.


from django.test import TestCase

from accelerator.tests.factories import ScenarioJudgeFactory


class TestScenarioJudge(TestCase):

    def test_str(self):
        scenario_judge = ScenarioJudgeFactory()
        assert str(scenario_judge.judge) in str(scenario_judge)
        assert str(scenario_judge.scenario) in str(scenario_judge)
