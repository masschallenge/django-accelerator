from django.db import models

from accelerator_abstract.models.accelerator_model import AcceleratorModel


class BaseEthnoRacialIdentity(AcceleratorModel):
    identity = models.CharField(max_length=100, blank=True, null=True)

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_ethnoracialidentity'
        abstract = True

    def __str__(self):
        return self.identity
