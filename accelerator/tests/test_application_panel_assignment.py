# MIT License
# Copyright (c) 2017 MassChallenge, Inc.


from django.test import TestCase

from accelerator.tests.factories.application_panel_assignment_factory \
    import ApplicationPanelAssignmentFactory


class TestApplicationPanelAssignment(TestCase):

    def setUp(self):
        self.apa = ApplicationPanelAssignmentFactory()

    def test_str(self):
        expected = u"{} -> {}".format(self.apa.application, self.apa.panel)
        self.assertEqual(str(self.apa), expected)
