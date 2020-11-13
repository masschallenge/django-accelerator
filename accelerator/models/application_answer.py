# MIT License
# Copyright (c) 2017 MassChallenge, Inc.


import swapper

from accelerator_abstract.models import BaseApplicationAnswer


class ApplicationAnswer(BaseApplicationAnswer):
    class Meta(BaseApplicationAnswer.Meta):
        swappable = swapper.swappable_setting(
            BaseApplicationAnswer.Meta.app_label, 'ApplicationAnswer')
