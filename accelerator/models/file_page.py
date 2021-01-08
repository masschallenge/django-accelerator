# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models.base_file_page import BaseFilePage


class FilePage(BaseFilePage):
    class Meta(BaseFilePage.Meta):
        swappable = False
