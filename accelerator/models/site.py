# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import swapper

from accelerator_abstract.models.accelerator_model import AcceleratorModel
import re
from django.db import models
from django.core.exceptions import ObjectDoesNotExist

from accelerator_abstract.models.base_site import BaseSite


class Site(BaseSite):
    class Meta(BaseSite.Meta):
        swappable = swapper.swappable_setting(
            BaseSite.Meta.app_label, "Site")
