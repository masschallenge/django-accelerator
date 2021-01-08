# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models import BaseApplicationAnswer


class ApplicationAnswer(BaseApplicationAnswer):
    class Meta(BaseApplicationAnswer.Meta):
        swappable = False
