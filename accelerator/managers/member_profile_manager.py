from django.db import models


class MemberProfileManager(models.Manager):

    def create(self, *args, **kwargs):
        profile = self.filter(user=kwargs['user']).first()
        if profile:
            profile.delete()
        return super(MemberProfileManager, self).create(*args, **kwargs)
