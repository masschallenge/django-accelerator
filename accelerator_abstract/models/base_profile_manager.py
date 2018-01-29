# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.db import models
from .base_profile_query_set import ProfileQuerySet


class ProfileManager(models.Manager):
    """provide a customized queryset
    """

    def get_queryset(self):
        # Breaking a circular reference:
        #   BaseProfile => ProfileManager => ProfileQuerySet => BaseProfile
        return ProfileQuerySet(self.model, using=self._db)
