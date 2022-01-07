from __future__ import unicode_literals

from accelerator_abstract.models.accelerator_model import AcceleratorModel


class LabelModel(AcceleratorModel):
    LABEL_LENGTH = 255
    pass

    class Meta(AcceleratorModel.Meta):
        abstract = True
