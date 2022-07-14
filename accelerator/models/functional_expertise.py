import swapper

from accelerator_abstract.models import BaseFunctionalExpertise


class FunctionalExpertise(BaseFunctionalExpertise):
    class Meta(BaseFunctionalExpertise.Meta):
        swappable = swapper.swappable_setting(
            BaseFunctionalExpertise.Meta.app_label, 'FunctionalExpertise')
