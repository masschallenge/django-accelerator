from __future__ import unicode_literals

import swapper

from factory import SubFactory
from factory.django import DjangoModelFactory

from accelerator.tests.factories.entrepreneur_factory import (
    EntrepreneurFactory
)
from accelerator.tests.factories.newsletter_factory import NewsletterFactory

NewsletterReceipt = swapper.load_model('accelerator', 'NewsletterReceipt')


class NewsletterReceiptFactory(DjangoModelFactory):
    class Meta:
        model = NewsletterReceipt

    newsletter = SubFactory(NewsletterFactory)
    recipient = SubFactory(EntrepreneurFactory)
