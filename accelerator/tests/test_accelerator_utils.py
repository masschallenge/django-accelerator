# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from django.test import TestCase
from accelerator.utils import url_validator
from django.core.exceptions import ValidationError


class TestAcceleratorUtils(TestCase):

    def test_url_validator_succeeds_for_proper_url(self):
        """
        this test will fail due to ValidationError
        if any of these are  invalid
        """
        validator = url_validator()
        validator("http://test.com")
        validator("http://test.org")
        validator("https://www.accelerate.masschallenge.org")
        validator("http://accelerate.masschallenge.org?test=3")

    def test_url_validator_fails_for_invalid_url(self):
        print("test")
        with self.assertRaises(
                ValidationError):
            validator = url_validator()
            validator("javascript://test.com")
