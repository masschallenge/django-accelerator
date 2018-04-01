# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import RefundCodeRedemptionFactory


class TestRefundCodeRedemption(TestCase):
    def test_str(self):
        redemption = RefundCodeRedemptionFactory()
        assert redemption.refund_code.unique_code in str(redemption)
