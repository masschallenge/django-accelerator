# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models import (
    BaseQuestion
)


class Question(BaseQuestion):
    class Meta(BaseQuestion.Meta):
        swappable = False
