# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase

from .factories import (
    NewsletterReceiptFactory,
)


class TestNewsletterReceipt(TestCase):

    def test_str(self):
        receipt = NewsletterReceiptFactory()
        assert receipt.newsletter.name in str(receipt)
