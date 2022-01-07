from __future__ import unicode_literals

import swapper

from accelerator_abstract.models import BaseUserLegalCheck


class UserLegalCheck(BaseUserLegalCheck):
    class Meta(BaseUserLegalCheck.Meta):
        swappable = swapper.swappable_setting(
            BaseUserLegalCheck.Meta.app_label, 'UserLegalCheck')
