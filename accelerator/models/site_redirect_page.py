# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import swapper

from accelerator_abstract.models.accelerator_model import AcceleratorModel
from django.db import models
from fluent_pages.models import Page

from accelerator_abstract.models.base_site_redirect_page import BaseSiteRedirectPage


class SiteRedirectPage(BaseSiteRedirectPage):
    class Meta(BaseSiteRedirectPage.Meta):
        swappable = swapper.swappable_setting(
            BaseSiteRedirectPage.Meta.app_label, "SiteRedirectPage")