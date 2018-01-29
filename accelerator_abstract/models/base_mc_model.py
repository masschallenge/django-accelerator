# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.conf import settings
from django.db import models


class MCModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta(object):
        abstract = True
        app_label = "mc"
        managed = settings.MCPROJECT_MODELS_ARE_MANAGED
