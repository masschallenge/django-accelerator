# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from django.db import models


class ProfileManager(models.Manager):
    """provide a customized queryset
    """

    def get_queryset(self):
        # Breaking a circular reference:
        #   BaseProfile => ProfileManager => ProfileQuerySet => BaseProfile
        from accelerator.models.profile_query_set import (
            ProfileQuerySet
        )
        return ProfileQuerySet(self.model, using=self._db)

    def create(self, *args, **kwargs):
        profile = self.filter(user=kwargs['user']).first()
        if profile:
            profile.delete()
        return super(ProfileManager, self).create(*args, **kwargs)
