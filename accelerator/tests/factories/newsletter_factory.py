from __future__ import unicode_literals

import swapper
from factory import (
    Sequence,
    SubFactory,
)
from factory.django import DjangoModelFactory

from accelerator.tests.factories.judging_round_factory import (
    JudgingRoundFactory
)
from accelerator.tests.factories.program_factory import ProgramFactory

Newsletter = swapper.load_model('accelerator', 'Newsletter')


class NewsletterFactory(DjangoModelFactory):
    class Meta:
        model = Newsletter

    name = Sequence(lambda n: "Newsletter {0}".format(n))
    subject = Sequence(lambda n: "NewsletterSubject {0}".format(n))
    from_addr = Sequence(lambda n: "staffer{0}@accelerator.org".format(n))
    program = SubFactory(ProgramFactory)
    judging_round = SubFactory(JudgingRoundFactory)
    cc_addrs = ""
    date_mailed = None
