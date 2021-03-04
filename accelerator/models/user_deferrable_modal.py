import swapper

from accelerator_abstract.models import BaseUserDeferrableModal


class UserDeferrableModal(BaseUserDeferrableModal):
    class Meta(BaseUserDeferrableModal.Meta):
        swappable = swapper.swappable_setting(
            BaseUserDeferrableModal.Meta.app_label, 'UserDeferrableModal'
        )
