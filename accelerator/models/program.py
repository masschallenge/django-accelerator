from __future__ import unicode_literals

import swapper

from accelerator_abstract.models import BaseProgram


class Program(BaseProgram):
    class Meta(BaseProgram.Meta):
        swappable = swapper.swappable_setting(BaseProgram.Meta.app_label,
                                              "Program")
