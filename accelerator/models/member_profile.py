from accelerator.managers.member_profile_manager import MemberProfileManager
from accelerator.models import CoreProfile


class MemberProfile(CoreProfile):
    user_type = 'member'
    default_page = "member_homepage"

    objects = MemberProfileManager()

    class Meta:
        db_table = 'accelerator_memberprofile'
