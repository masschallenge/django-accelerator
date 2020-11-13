# MIT License
# Copyright (c) 2017 MassChallenge, Inc.


import swapper

from accelerator_abstract.models.base_application import BaseApplication


class Application(BaseApplication):
    class Meta(BaseApplication.Meta):
        swappable = swapper.swappable_setting(
            BaseApplication.Meta.app_label, 'Application')
