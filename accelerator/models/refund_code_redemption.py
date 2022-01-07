from __future__ import unicode_literals

import swapper

from accelerator_abstract.models.base_refund_code_redemption import (
    BaseRefundCodeRedemption
)


class RefundCodeRedemption(BaseRefundCodeRedemption):
    class Meta(BaseRefundCodeRedemption.Meta):
        swappable = swapper.swappable_setting(
            BaseRefundCodeRedemption.Meta.app_label, "RefundCodeRedemption")
