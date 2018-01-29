# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import swapper

from accelerator_abstract.models import BaseFunctionalExpertise
from accelerator_abstract.models.accelerator_model import AcceleratorModel
from django.db import models

from mptt.models import MPTTModel
from mptt.models import TreeForeignKey


class FunctionalExpertise(BaseFunctionalExpertise):
    class Meta(BaseFunctionalExpertise.Meta):
        swappable = 'MPTT_SWAPPABLE_FUNCTIONALEXPERTISE_MODEL'
