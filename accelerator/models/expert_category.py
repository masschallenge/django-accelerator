# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import swapper

from accelerator_abstract.models import BaseExpertCategory
from accelerator_abstract.models.accelerator_model import AcceleratorModel
from django.db import models


class ExpertCategory(BaseExpertCategory):
    class Meta(BaseExpertCategory.Meta):
        swappable = swapper.swappable_setting(
            BaseExpertCategory.Meta.app_label, "ExpertCategory")
