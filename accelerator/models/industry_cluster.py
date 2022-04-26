from sorl.thumbnail import ImageField
from django.db.models import (
    CharField,
    TextField,
    PositiveIntegerField,
)

from accelerator_abstract.models.accelerator_model import AcceleratorModel


class IndustryCluster(AcceleratorModel):
    name = CharField(max_length=255)
    description = TextField()
    image = ImageField(
        upload_to='industry_cluster_images',
        blank=True, null=True)
    display_priority = PositiveIntegerField()
