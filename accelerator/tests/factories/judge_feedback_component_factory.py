# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from factory import (
    Sequence,
    SubFactory,
)
from factory.django import DjangoModelFactory

from accelerator.models import JudgeFeedbackComponent
from accelerator.tests.factories.judge_application_feedback_factory import (
    JudgeApplicationFeedbackFactory,
)
from accelerator.tests.factories.judging_form_element_factory import (
    JudgingFormElementFactory
)


class JudgeFeedbackComponentFactory(DjangoModelFactory):
    class Meta:
        model = JudgeFeedbackComponent

    judge_feedback = SubFactory(JudgeApplicationFeedbackFactory)
    feedback_element = SubFactory(JudgingFormElementFactory)
    answer_text = Sequence(lambda n: "Judge Answer Text {0}".format(n))
