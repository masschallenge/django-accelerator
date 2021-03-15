# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import (
    SubFactory,
    post_generation,
)
from factory.django import DjangoModelFactory

from accelerator.accelerator.models import (
    JUDGING_FEEDBACK_STATUS_INCOMPLETE,
    JUDGING_STATUS_NO_CONFLICT,
)
from accelerator.accelerator.tests.factories.application_factory import ApplicationFactory
from accelerator.accelerator.tests.factories.expert_factory import ExpertFactory
from accelerator.accelerator.tests.factories.judging_form_factory import JudgingFormFactory
from accelerator.accelerator.tests.factories.panel_factory import PanelFactory

JudgeApplicationFeedback = swapper.load_model('accelerator',
                                              'JudgeApplicationFeedback')


class JudgeApplicationFeedbackFactory(DjangoModelFactory):
    class Meta:
        model = JudgeApplicationFeedback
        django_get_or_create = ('application', 'judge', 'panel')

    application = SubFactory(ApplicationFactory)
    form_type = SubFactory(JudgingFormFactory)
    judge = SubFactory(ExpertFactory)
    panel = SubFactory(PanelFactory)
    judging_status = JUDGING_STATUS_NO_CONFLICT
    feedback_status = JUDGING_FEEDBACK_STATUS_INCOMPLETE

    @post_generation
    def viewers(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for viewer in extracted:
                self.viewers.add(viewer)
