# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import swapper

from accelerator_abstract.models import BaseMentoringSpecialties
from accelerator_abstract.models.accelerator_model import AcceleratorModel
from django.db import models


class MentoringSpecialties(BaseMentoringSpecialties):
    class Meta(BaseMentoringSpecialties.Meta):
        swappable = swapper.swappable_setting(
            BaseMentoringSpecialties.Meta.app_label, "MentoringSpecialties")
