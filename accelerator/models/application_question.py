# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import swapper

from django.db import models
from accelerator_abstract.models import (
    BaseApplicationQuestion,
    CHOICE_LAYOUTS,
    QUESTION_TYPES,
)

from accelerator_abstract.models.accelerator_model import AcceleratorModel

CHARACTERS_UNIT_NAME = "Characters"
WORDS_UNIT_NAME = "Words"
TEXT_LIMIT_UNITS = ((CHARACTERS_UNIT_NAME.lower(), CHARACTERS_UNIT_NAME),
                    (WORDS_UNIT_NAME.lower(), WORDS_UNIT_NAME))


@python_2_unicode_compatible
class ApplicationQuestion(BaseApplicationQuestion):
    class Meta(AcceleratorModel.Meta):
        swappable = swapper.swappable_setting(
            BaseApplicationQuestion.Meta.app_label, "ApplicationQuestion")
