# MIT License
# Copyright (c) 2017 MassChallenge, Inc.


import swapper

from accelerator_abstract.models.base_site_redirect_page import (
    BaseSiteRedirectPage
)


class SiteRedirectPage(BaseSiteRedirectPage):
    class Meta(BaseSiteRedirectPage.Meta):
        swappable = swapper.swappable_setting(
            BaseSiteRedirectPage.Meta.app_label, "SiteRedirectPage")
