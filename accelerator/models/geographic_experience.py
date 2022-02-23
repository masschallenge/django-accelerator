from django.db import models
from accelerator_abstract.models.accelerator_model import AcceleratorModel


class GeographicExperience(AcceleratorModel):
    name = models.CharField(max_length=255)

    def __repr__(self):
        return 'Geographic Experience: {}'.format(self.name)
