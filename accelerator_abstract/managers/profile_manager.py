from django.db import models


class ProfileManager(models.Manager):
    """provide a customized queryset
    """

    def get_queryset(self):
        # Breaking a circular reference:
        #   BaseProfile => ProfileManager => ProfileQuerySet => BaseProfile
        from accelerator_abstract.models.profile_query_set import (
            ProfileQuerySet
        )
        return ProfileQuerySet(self.model, using=self._db)
