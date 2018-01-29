# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import swapper

from accelerator_abstract.models.accelerator_model import AcceleratorModel
from django.template.defaultfilters import slugify
from collections import OrderedDict
from django.db import models

from accelerator_abstract.models.base_program_startup_attribute import BaseProgramStartupAttribute


class ProgramStartupAttribute(BaseProgramStartupAttribute):
    class Meta(BaseProgramStartupAttribute.Meta):
        swappable = swapper.swappable_setting(
            BaseProgramStartupAttribute.Meta.app_label, "ProgramStartupAttribute")
