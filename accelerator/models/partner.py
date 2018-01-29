# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import swapper

from accelerator_abstract.models import BasePartner
from accelerator_abstract.models.accelerator_model import AcceleratorModel
from django.db import models
from django.core.exceptions import ObjectDoesNotExist

from sorl.thumbnail import ImageField


class Partner(BasePartner):
    class Meta(BasePartner.Meta):
        swappable = swapper.swappable_setting(
            BasePartner.Meta.app_label, "Partner")
