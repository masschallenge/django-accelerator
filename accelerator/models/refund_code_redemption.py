# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models.base_refund_code_redemption import (
    BaseRefundCodeRedemption
)


class RefundCodeRedemption(BaseRefundCodeRedemption):
    class Meta(BaseRefundCodeRedemption.Meta):
        swappable = False
