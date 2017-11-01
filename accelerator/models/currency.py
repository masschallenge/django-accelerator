# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.conf import settings
from accelerator_abstract.models import BaseCurrency
import swapper


class Currency(BaseCurrency):
    class Meta:
        db_table = 'accelerator_currency'
        managed = settings.ACCELERATOR_MODELS_ARE_MANAGED
        swappable = swapper.swappable_setting('accelerator',
                                              'Currency')
