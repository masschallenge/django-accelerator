# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models import BaseProgramFamily


class ProgramFamily(BaseProgramFamily):
    class Meta(BaseProgramFamily.Meta):
        swappable = False
