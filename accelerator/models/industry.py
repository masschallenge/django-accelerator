import swapper
from accelerator_abstract.models import BaseIndustry


class Industry(BaseIndustry):
    class Meta(BaseIndustry.Meta):
        swappable = swapper.swappable_setting(
            BaseIndustry.Meta.app_label, 'Industry')
