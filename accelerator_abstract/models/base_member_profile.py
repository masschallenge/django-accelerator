# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible

from accelerator_abstract.models.base_core_profile import BaseCoreProfile


@python_2_unicode_compatible
class BaseMemberProfile(BaseCoreProfile):
    user_type = 'member'
    default_page = "member_homepage"

    class Meta(BaseCoreProfile.Meta):
        db_table = '{}_memberprofile'.format(
            BaseCoreProfile.Meta.app_label)
        abstract = True
