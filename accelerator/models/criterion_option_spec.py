# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models.base_criterion_option_spec import (
    BaseCriterionOptionSpec,
)


class CriterionOptionSpec(BaseCriterionOptionSpec):
    class Meta(BaseCriterionOptionSpec.Meta):
        swappable = False
