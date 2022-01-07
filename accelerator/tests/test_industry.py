from django.test import TestCase

from .factories.industry_factory import IndustryFactory


class TestIndustry(TestCase):
    def test_industry(self):
        parent = IndustryFactory()
        industry = IndustryFactory(parent=parent)
        self.assertTrue(industry.name in str(industry))
        self.assertTrue(industry.parent.name in str(industry))
