from __future__ import unicode_literals

import swapper

from accelerator_abstract.models import BaseReference
from accelerator_abstract.models.accelerator_model import AcceleratorModel


class Reference(BaseReference):
    class Meta(AcceleratorModel.Meta):
        swappable = swapper.swappable_setting(
            AcceleratorModel.Meta.app_label, "Reference")
