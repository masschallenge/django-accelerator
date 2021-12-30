from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import PanelFactory


class TesPanel(TestCase):

    def test_str(self):
        panel = PanelFactory()
        assert panel.description in str(panel)

    def test_str_no_description(self):
        panel = PanelFactory(description='')
        assert str(panel.panel_type) in str(panel)
        assert str(panel.panel_time) in str(panel)

    def test_str_no_description_no_panel_type(self):
        panel = PanelFactory(description='',
                             panel_type=None)
        assert str(panel.panel_time) not in str(panel)
        assert str(panel.id) in str(panel)
