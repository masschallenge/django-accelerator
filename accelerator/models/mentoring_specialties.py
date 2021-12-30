from __future__ import unicode_literals

import swapper

from accelerator_abstract.models import BaseMentoringSpecialties


class MentoringSpecialties(BaseMentoringSpecialties):
    class Meta(BaseMentoringSpecialties.Meta):
        swappable = swapper.swappable_setting(
            BaseMentoringSpecialties.Meta.app_label, "MentoringSpecialties")
