# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models.base_site_redirect_page import (
    BaseSiteRedirectPage
)


class SiteRedirectPage(BaseSiteRedirectPage):
    class Meta(BaseSiteRedirectPage.Meta):
        swappable = False
