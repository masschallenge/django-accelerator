import swapper
from django.db import models

from accelerator.models import CoreProfile


class CoreProfilePtrModel(models.Model):
    coreprofile_ptr = models.OneToOneField(
        swapper.get_model_name('accelerator', 'CoreProfile'),
        on_delete=models.deletion.CASCADE,
        parent_link=True,
    )

    class Meta:
        abstract = True


class EntrepreneurProfile1(CoreProfilePtrModel, CoreProfile):
    user_type = 'entrepreneur'
    default_page = "applicant_homepage"

    class Meta:
        db_table = 'accelerator_entrepreneurprofile1'
        swappable = swapper.swappable_setting(
            "accelerator", "EntrepreneurProfile1")
