# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from accelerator_abstract.models import BaseProgramFamily
from accelerator_abstract.models.accelerator_model import AcceleratorModel


@python_2_unicode_compatible
class ProgramFamily(BaseProgramFamily):
    class Meta(BaseProgramFamily.Meta):
        swappable = swapper.swappable_setting(
            BaseProgramFamily.Meta.app_label, "ProgramFamily")
