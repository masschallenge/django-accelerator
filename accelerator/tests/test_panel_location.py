from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import PanelLocationFactory


class TestPanelLocation(TestCase):

    def test_str(self):
        panel_location = PanelLocationFactory()
        assert panel_location.description in str(panel_location)
