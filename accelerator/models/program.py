# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

import swapper

from accelerator_abstract.models import BaseProgram


@python_2_unicode_compatible
class Program(BaseProgram):
    class Meta(BaseProgram.Meta):
        swappable = swapper.swappable_setting(BaseProgram.Meta.app_label,
                                              "Program")
