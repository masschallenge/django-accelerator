# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models.base_category_header_page import (
    BaseCategoryHeaderPage
)


class CategoryHeaderPage(BaseCategoryHeaderPage):
    class Meta(BaseCategoryHeaderPage.Meta):
        swappable = False
