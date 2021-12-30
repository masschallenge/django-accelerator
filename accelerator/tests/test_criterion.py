from __future__ import unicode_literals

from django.test import TestCase

from .factories import (
    CriterionFactory
)


class TestCriterion(TestCase):

    def test_str(self):
        criterion = CriterionFactory()
        assert criterion.name in str(criterion)
