# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import swapper

from accelerator_abstract.models.accelerator_model import AcceleratorModel
from django.conf import settings
from django.db import models
from fluent_pages.models import Page

# customized storage that places CMS files outside of url space so we can
# control access via the FilePage object to which they are attached.
from accelerator_abstract.models.secure_file_system_storage import (
    SecureFileSystemStorage
)

cms_fs = SecureFileSystemStorage(location=settings.CMS_FILE_ROOT)


class BaseFilePage(Page, AcceleratorModel):
    file = models.FileField(storage=cms_fs, upload_to="%Y-%m")
    description = models.TextField(blank=True)

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_filepage'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True
        verbose_name = "File"
        verbose_name_plural = "Files"
