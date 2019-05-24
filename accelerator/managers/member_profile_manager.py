import logging

from django.db import models


logger = logging.getLogger(__file__)
MEMBER_PROFILE_RECREATION_WARNING = (
    "Request made for MemberProfile creation "
    "for user, {user}, already with profile. Recreating new MemberProfile."
)


class MemberProfileManager(models.Manager):

    def create(self, *args, **kwargs):
        self.filter(user=kwargs['user']).delete()
        logger.info(MEMBER_PROFILE_RECREATION_WARNING.format(
            user=kwargs['user']))
        return super(MemberProfileManager, self).create(*args, **kwargs)
