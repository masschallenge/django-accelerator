# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
import swapper

from accelerator_abstract.models import (
    BaseApplicationQuestion,
    CHOICE_LAYOUTS,
    QUESTION_TYPES,
)

from accelerator_abstract.models.accelerator_model import AcceleratorModel


class ApplicationQuestion(BaseApplicationQuestion):
    class Meta(AcceleratorModel.Meta):
        swappable = swapper.swappable_setting(
            BaseApplicationQuestion.Meta.app_label, "ApplicationQuestion")
