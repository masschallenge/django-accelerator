# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

import logging

from django.db import models


logger = logging.getLogger(__file__)
PROFILE_CREATION_WARNING = (
    "Request made for {profile_type}Profile creation "
    "for user, {user}, already with MemberProfile. "
    "Deleted existing MemberProfile and creating new {profile_type}Profile."
)


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
        self.filter(user=kwargs['user'], user_type="MEMBER").delete()
        logger.info(PROFILE_CREATION_WARNING.format(
            profile_type=kwargs['user_type'].title(),
            user=kwargs['user']))
        return super(ProfileManager, self).create(*args, **kwargs)
