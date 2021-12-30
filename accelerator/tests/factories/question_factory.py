from __future__ import unicode_literals

import swapper
from factory import Sequence
from factory.django import DjangoModelFactory

from accelerator.models import (
    CHOICE_LAYOUT_HORIZONTAL,
    QUESTION_TYPE_MULTILINE,
)

Question = swapper.load_model('accelerator', 'Question')


class QuestionFactory(DjangoModelFactory):
    class Meta:
        model = Question

    name = Sequence(lambda n: "Question {0}".format(n))
    question_type = QUESTION_TYPE_MULTILINE
    choice_options = ""
    choice_layout = CHOICE_LAYOUT_HORIZONTAL
