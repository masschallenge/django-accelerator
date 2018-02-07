import swapper
from factory import (
    DjangoModelFactory,
    Sequence,
    SubFactory,
)

from accelerator.apps import AcceleratorConfig

ApplicationAnswer = swapper.load_model(AcceleratorConfig.name,
                                       'ApplicationAnswer')

from accelerator.tests.factories.application_factory import ApplicationFactory
from accelerator.tests.factories.application_question_factory import (
    ApplicationQuestionFactory
)


class ApplicationAnswerFactory(DjangoModelFactory):
    class Meta:
        model = ApplicationAnswer

    application = SubFactory(ApplicationFactory)
    application_question = SubFactory(ApplicationQuestionFactory)
    answer_text = Sequence(lambda n: "Answer Text {0}".format(n))
