from __future__ import unicode_literals

import swapper

from accelerator_abstract.models import BaseBusinessProposition


class BusinessProposition(BaseBusinessProposition):
    class Meta(BaseBusinessProposition.Meta):
        pass
