from __future__ import unicode_literals

import swapper

from accelerator_abstract.models.base_criterion_option_spec import (
    BaseCriterionOptionSpec,
)


class CriterionOptionSpec(BaseCriterionOptionSpec):
    class Meta(BaseCriterionOptionSpec.Meta):
        swappable = swapper.swappable_setting(
            BaseCriterionOptionSpec.Meta.app_label, "CriterionOptionSpec")
