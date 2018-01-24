# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from django.conf import settings
from django.db import models


class AcceleratorModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta(object):
        abstract = True
        app_label = "accelerator"
        managed = settings.ACCELERATOR_MODELS_ARE_MANAGED
