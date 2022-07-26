from django.db import models
from accelerator_abstract.models.accelerator_model import AcceleratorModel


class Ecosystem(AcceleratorModel):
    name = models.CharField(max_length=50)
    is_visible = models.BooleanField(default=True)
    display_priority = models.PositiveIntegerField()
