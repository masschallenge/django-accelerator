from __future__ import unicode_literals

import swapper

from accelerator_abstract.models.base_category_header_page import (
    BaseCategoryHeaderPage
)


class CategoryHeaderPage(BaseCategoryHeaderPage):
    class Meta(BaseCategoryHeaderPage.Meta):
        swappable = swapper.swappable_setting(
            BaseCategoryHeaderPage.Meta.app_label, "CategoryHeaderPage")
