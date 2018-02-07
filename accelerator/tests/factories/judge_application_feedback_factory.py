# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import (
    DjangoModelFactory,
    SubFactory,
    post_generation,
)

from accelerator.apps import AcceleratorConfig
from accelerator.models import JUDGING_STATUS_NO_CONFLICT

JudgeApplicationFeedback = swapper.load_model(AcceleratorConfig.name,
                                              'JudgeApplicationFeedback')

from accelerator.tests.factories.application_factory import ApplicationFactory
from accelerator.tests.factories.expert_factory import ExpertFactory
from accelerator.tests.factories.judging_form_factory import JudgingFormFactory
from accelerator.tests.factories.panel_factory import PanelFactory


class JudgeApplicationFeedbackFactory(DjangoModelFactory):
    class Meta:
        model = JudgeApplicationFeedback

    application = SubFactory(ApplicationFactory)
    form_type = SubFactory(JudgingFormFactory)
    judge = SubFactory(ExpertFactory)
    panel = SubFactory(PanelFactory)
    judging_status = JUDGING_STATUS_NO_CONFLICT

    @post_generation
    def viewers(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for viewer in extracted:
                self.viewers.add(viewer)
