import swapper
from accelerator_abstract.models import BaseDeferrableModal


class DeferrableModal(BaseDeferrableModal):

    class Meta(BaseDeferrableModal.Meta):
        swappable = swapper.swappable_setting(
            BaseDeferrableModal.Meta.app_label, 'DeferrableModal'
        )
