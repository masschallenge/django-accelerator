from __future__ import unicode_literals

import swapper

from accelerator_abstract.models import BaseNewsletterReceipt


class NewsletterReceipt(BaseNewsletterReceipt):
    class Meta(BaseNewsletterReceipt.Meta):
        swappable = swapper.swappable_setting(
            BaseNewsletterReceipt.Meta.app_label, "NewsletterReceipt")
