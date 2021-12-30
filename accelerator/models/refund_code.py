from __future__ import unicode_literals

import swapper

from accelerator_abstract.models.base_refund_code import BaseRefundCode


class RefundCode(BaseRefundCode):
    class Meta(BaseRefundCode.Meta):
        swappable = swapper.swappable_setting(
            BaseRefundCode.Meta.app_label, "RefundCode")
