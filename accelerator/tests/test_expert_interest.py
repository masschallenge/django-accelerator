# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.test import TestCase

from accelerator.tests.factories import (
    EntrepreneurFactory,
    ExpertInterestFactory,
)
from accelerator_abstract.models.base_expert_interest import (
    is_expert_validator,
)


class TestExpertInterest(TestCase):
    def test_str(self):
        obj = ExpertInterestFactory()
        name = str(obj)
        assert str(obj.interest_type) in name
        assert str(obj.user) in name
        assert str(obj.program_family) in name

    # Testing the validator directly since I couldn't get the
    # factories to run it.
    def test_experts_only(self):
        user = EntrepreneurFactory()
        with self.assertRaises(ValidationError):
            is_expert_validator(user.id)
