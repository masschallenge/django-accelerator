# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import (
    DjangoModelFactory,
    Sequence,
    SubFactory,
)

from accelerator.apps import AcceleratorConfig
from accelerator.tests.factories.judge_application_feedback_factory import (
    JudgeApplicationFeedbackFactory,
)
from accelerator.tests.factories.judging_form_element_factory import (
    JudgingFormElementFactory
)

JudgeFeedbackComponent = swapper.load_model(AcceleratorConfig.name,
                                            'JudgeFeedbackComponent')


class JudgeFeedbackComponentFactory(DjangoModelFactory):
    class Meta:
        model = JudgeFeedbackComponent

    judge_feedback = SubFactory(JudgeApplicationFeedbackFactory)
    feedback_element = SubFactory(JudgingFormElementFactory)
    answer_text = Sequence(lambda n: "Judge Answer Text {0}".format(n))
