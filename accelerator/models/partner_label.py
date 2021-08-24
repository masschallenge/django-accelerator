from __future__ import unicode_literals

import swapper

from accelerator_abstract.models import BasePartnerLabel
from accelerator_abstract.models.label_model import LabelModel


class PartnerLabel(BasePartnerLabel):
    class Meta(LabelModel.Meta):
        swappable = swapper.swappable_setting(BasePartnerLabel.Meta.app_label,
                                              "PartnerLabel")
