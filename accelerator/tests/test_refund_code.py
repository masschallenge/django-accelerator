# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import RefundCodeFactory


class TestRefundCode(TestCase):

    def test_str(self):
        refund_code = RefundCodeFactory()
        assert refund_code.unique_code in str(refund_code)
