# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper

from accelerator_abstract.models.base_file_page import BaseFilePage


class FilePage(BaseFilePage):
    class Meta(BaseFilePage.Meta):
        swappable = swapper.swappable_setting(
            BaseFilePage.Meta.app_label, "FilePage")
        abstract = True
        verbose_name = "File"
        verbose_name_plural = "Files"
