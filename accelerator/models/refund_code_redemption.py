# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper

from accelerator_abstract.models.base_refund_code_redemption import (
    BaseRefundCodeRedemption
)

CREDIT_CODE_NOT_AVAILABLE = ("Apologies, credit code %s "
                             "is no longer available")


class RefundCodeRedemption(BaseRefundCodeRedemption):
    class Meta(BaseRefundCodeRedemption.Meta):
        swappable = swapper.swappable_setting(
            BaseRefundCodeRedemption.Meta.app_label, "RefundCodeRedemption")
