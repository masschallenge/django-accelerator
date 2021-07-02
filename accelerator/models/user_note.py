import swapper
from accelerator_abstract.models import BaseUserNote


class UserNote(BaseUserNote):
    class Meta(BaseUserNote.Meta):
        swappable = swapper.swappable_setting(
            BaseUserNote.Meta.app_label, "UserNote"
        )
