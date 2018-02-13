# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import (
    DjangoModelFactory,
    SubFactory,
)

from accelerator.apps import AcceleratorConfig
from accelerator.tests.factories.entrepreneur_factory import (
    EntrepreneurFactory
)
from accelerator.tests.factories.newsletter_factory import NewsletterFactory

NewsletterReceipt = swapper.load_model(AcceleratorConfig.name,
                                       'NewsletterReceipt')


class NewsletterReceiptFactory(DjangoModelFactory):
    class Meta:
        model = NewsletterReceipt

    newsletter = SubFactory(NewsletterFactory)
    recipient = SubFactory(EntrepreneurFactory)
