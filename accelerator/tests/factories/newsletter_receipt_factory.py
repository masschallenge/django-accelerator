import swapper
from factory import (
    DjangoModelFactory,
    SubFactory,
)

from accelerator.apps import AcceleratorConfig

NewsletterReceipt = swapper.load_model(AcceleratorConfig.name,
                                       'NewsletterReceipt')

from accelerator.tests.factories.entrepreneur_factory import EntrepreneurFactory
from accelerator.tests.factories.newsletter_factory import NewsletterFactory


class NewsletterReceiptFactory(DjangoModelFactory):
    class Meta:
        model = NewsletterReceipt

    newsletter = SubFactory(NewsletterFactory)
    recipient = SubFactory(EntrepreneurFactory)
