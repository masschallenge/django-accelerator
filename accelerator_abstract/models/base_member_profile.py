from __future__ import unicode_literals

from accelerator_abstract.models.base_core_profile import BaseCoreProfile


class BaseMemberProfile(BaseCoreProfile):
    user_type = 'member'
    default_page = "member_homepage"

    class Meta(BaseCoreProfile.Meta):
        db_table = 'accelerator_memberprofile'
        abstract = True
