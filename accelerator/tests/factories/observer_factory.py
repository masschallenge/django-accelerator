import swapper
from factory import (
    DjangoModelFactory,
    Sequence,
    post_generation,
)

from accelerator.apps import AcceleratorConfig

Observer = swapper.load_model(AcceleratorConfig.name, 'Observer')


class ObserverFactory(DjangoModelFactory):
    first_name = Sequence(lambda n: "First {0}".format(n))
    last_name = Sequence(lambda n: "Last {0}".format(n))
    email = Sequence(lambda n: "user_{0}@example.com".format(n))
    title = Sequence(lambda n: "Observer title %d" % n)
    company = Sequence(lambda n: "Observer company %d" % n)
    newsletter_sender = False

    class Meta:
        model = Observer

    @post_generation
    def newsletter_cc_roles(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for tag in extracted:
                self.newsletter_cc_roles.add(tag)
