import swapper

from accelerator_abstract.models import BasePartnerApplicationInterest


class PartnerApplicationInterest(BasePartnerApplicationInterest):
    class Meta(BasePartnerApplicationInterest.Meta):
        swappable = swapper.swappable_setting(
            BasePartnerApplicationInterest.Meta.app_label,
            "PartnerApplicationInterest")
