import swapper
from accelerator_abstract.models import BaseNote


class Note(BaseNote):
    class Meta(BaseNote.Meta):
        swappable = swapper.swappable_setting(
            BaseNote.Meta.app_label, "Note"
        )
