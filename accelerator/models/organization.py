from __future__ import unicode_literals

import swapper

from accelerator_abstract.models import BaseOrganization


class Organization(BaseOrganization):
    class Meta(BaseOrganization.Meta):
        swappable = swapper.swappable_setting(BaseOrganization.Meta.app_label,
                                              'Organization')
