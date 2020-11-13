# MIT License
# Copyright (c) 2017 MassChallenge, Inc.


import swapper

from accelerator_abstract.models.base_file_page import BaseFilePage


class FilePage(BaseFilePage):
    class Meta(BaseFilePage.Meta):
        swappable = swapper.swappable_setting(
            BaseFilePage.Meta.app_label, "FilePage")
