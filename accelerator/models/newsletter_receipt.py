# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models import BaseNewsletterReceipt


class NewsletterReceipt(BaseNewsletterReceipt):
    class Meta(BaseNewsletterReceipt.Meta):
        swappable = False
