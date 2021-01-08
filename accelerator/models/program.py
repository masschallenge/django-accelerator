# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models import BaseProgram


class Program(BaseProgram):
    class Meta(BaseProgram.Meta):
        swappable = False
