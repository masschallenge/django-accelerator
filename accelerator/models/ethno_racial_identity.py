import swapper
from accelerator_abstract.models.base_ethno_racial_identity import (
    BaseEthnoRacialIdentity,
)


class EthnoRacialIdentity(BaseEthnoRacialIdentity):
    class Meta(BaseEthnoRacialIdentity.Meta):
        swappable = swapper.swappable_setting(
            BaseEthnoRacialIdentity.Meta.app_label, 'EthnoRacialIdentity')
