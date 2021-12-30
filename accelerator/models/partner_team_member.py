from __future__ import unicode_literals

import swapper

from accelerator_abstract.models import BasePartnerTeamMember


class PartnerTeamMember(BasePartnerTeamMember):
    class Meta(BasePartnerTeamMember.Meta):
        swappable = swapper.swappable_setting(
            BasePartnerTeamMember.Meta.app_label, "PartnerTeamMember")
