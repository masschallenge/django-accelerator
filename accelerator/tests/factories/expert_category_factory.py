from __future__ import unicode_literals

import swapper
from factory import Iterator
from factory.django import DjangoModelFactory

from accelerator.models import VALID_EXPERT_CATEGORIES

# The import of VALID_EXPERT_CATEGORIES is indicative of a deeper problem with
# how ExpertCategorys are currently used.  See AC-5022 for the underlying
# issue and a discussion of possible better long term solutions.

ExpertCategory = swapper.load_model('accelerator', 'ExpertCategory')


class ExpertCategoryFactory(DjangoModelFactory):
    class Meta:
        model = ExpertCategory
        django_get_or_create = ('name',)

    name = Iterator(VALID_EXPERT_CATEGORIES)
