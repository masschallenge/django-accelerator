# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models import BaseProgramOverride


class ProgramOverride(BaseProgramOverride):
    class Meta(BaseProgramOverride.Meta):
        swappable = False
