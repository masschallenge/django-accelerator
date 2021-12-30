from __future__ import unicode_literals

import swapper

from accelerator_abstract.models import BaseStartup


class Startup(BaseStartup):
    class Meta(BaseStartup.Meta):
        swappable = swapper.swappable_setting(BaseStartup.Meta.app_label,
                                              'Startup')
