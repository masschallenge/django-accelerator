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


class EntrepreneurProfile(CoreProfile):
    user_type = 'entrepreneur'
    default_page = "applicant_homepage"

    class Meta:
        db_table = 'accelerator_entrepreneurprofile'
