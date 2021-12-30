from __future__ import unicode_literals

import swapper
from factory import (
    Sequence,
    SubFactory,
)
from factory.django import DjangoModelFactory

from accelerator.tests.factories.application_factory import ApplicationFactory
from accelerator.tests.factories.application_question_factory import (
    ApplicationQuestionFactory
)

ApplicationAnswer = swapper.load_model('accelerator', 'ApplicationAnswer')


class ApplicationAnswerFactory(DjangoModelFactory):
    class Meta:
        model = ApplicationAnswer

    application = SubFactory(ApplicationFactory)
    application_question = SubFactory(ApplicationQuestionFactory)
    answer_text = Sequence(lambda n: "Answer Text {0}".format(n))
