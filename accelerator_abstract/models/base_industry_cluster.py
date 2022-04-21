from sorl.thumbnail import ImageField
from django.db.models import (
    CharField,
    TextField,
)

from accelerator_abstract.models.accelerator_model import AcceleratorModel


class BaseIndustryCluster(AcceleratorModel):
    name = CharField(max_length=255)
    description = TextField()
    image = ImageField(
        upload_to='industry_cluster_images',
        blank=True, null=True)

    class Meta(AcceleratorModel.Meta):
        verbose_name_plural = 'Industry Clusters'
        db_table = 'accelerator_industrycluster'
        abstract = True
