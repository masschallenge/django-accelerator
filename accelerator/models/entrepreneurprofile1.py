import swapper
from django.db import models

from accelerator.models import CoreProfile
"""
Plan:
add new model EntrepreneurProfile1(inheriting from coreprofile) while keeping EntrepreneurProfile and make migrations
add data migrations to copy data from EntrepreneurProfile to EntrepreneurProfile1
delete  EntrepreneurProfile  and make migrations
Rename EntrepreneurProfile1 to EntrepreneurProfile and make migrations
"""

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
