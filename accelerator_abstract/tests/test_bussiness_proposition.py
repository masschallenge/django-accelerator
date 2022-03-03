from django.test import TestCase

from accelerator.tests.factories import (
    BusinessPropositionFactory
)
from accelerator.models import BusinessProposition
from accelerator.accelerator_abstract.models import EXCLUDED_FIELDS


class TestBussinessProposition(TestCase):
    def test_return_false_with_incomplete_text(self):
        bussiness_proposition = BusinessPropositionFactory()
        self.assertFalse(bussiness_proposition.complete())
    
    def populate_data(self):
        fields = BusinessProposition._meta.get_fields(include_parents=False)
        characters = 'This is a more than 20 character texts'
        data = {}
        for field in fields:
            if field.name not in EXCLUDED_FIELDS:
                data[field.name] = characters
        return data

    def test_return_true_with_complete_text(self):
        data = self.populate_data(bussiness_proposition)
        bussiness_proposition = BusinessPropositionFactory(**data)
        self.assertTrue(bussiness_proposition.complete())
