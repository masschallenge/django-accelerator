import swapper
from factory import (
    DjangoModelFactory,
    Sequence,
    SubFactory,
)

from accelerator.apps import AcceleratorConfig

Newsletter = swapper.load_model(AcceleratorConfig.name, 'Newsletter')

from accelerator.tests.factories.program_factory import ProgramFactory
from accelerator.tests.factories.judging_round_factory import JudgingRoundFactory


class NewsletterFactory(DjangoModelFactory):
    class Meta:
        model = Newsletter

    name = Sequence(lambda n: "Newsletter {0}".format(n))
    subject = Sequence(lambda n: "NewsletterSubject {0}".format(n))
    from_addr = Sequence(lambda n: "mcstaffer{0}@mc.org".format(n))
    program = SubFactory(ProgramFactory)
    judging_round = SubFactory(JudgingRoundFactory)
    cc_addrs = ""
    date_mailed = None
