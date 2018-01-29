# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import swapper

from accelerator_abstract.models import BaseJudgingFormElement
from accelerator_abstract.models.accelerator_model import AcceleratorModel
from django.db import models


class JudgingFormElement(BaseJudgingFormElement):
    class Meta(BaseJudgingFormElement.Meta):
        swappable = swapper.swappable_setting(
            BaseJudgingFormElement.Meta.app_label, "JudgingFormElement")
