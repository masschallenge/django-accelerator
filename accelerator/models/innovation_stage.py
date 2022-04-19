from django.db import models
from sorl.thumbnail import ImageField

from accelerator_abstract.models.accelerator_model import AcceleratorModel


class InnovationStage(AcceleratorModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = ImageField(
        upload_to='innovation_stage_images', blank=True, null=True)
    display_priority = models.PositiveIntegerField()
