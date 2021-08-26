from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import PartnerLabelFactory


class TestPartnerLabel(TestCase):
    def test_str(self):
        label = PartnerLabelFactory()
        assert label.label in str(label)
