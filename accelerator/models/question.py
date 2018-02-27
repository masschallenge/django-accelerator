# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper

from accelerator_abstract.models import (
    BaseQuestion
)


class Question(BaseQuestion):
    class Meta(BaseQuestion.Meta):
        swappable = swapper.swappable_setting(BaseQuestion.Meta.app_label,
                                              "Question")
