# MIT License
# Copyright (c) 2017 MassChallenge, Inc.


from django.db import models

from accelerator_abstract.models.base_core_profile import BaseCoreProfile


class BaseEntrepreneurProfile(BaseCoreProfile):
    user_type = 'entrepreneur'
    default_page = "applicant_homepage"
    bio = models.TextField(blank=True, default="")

    class Meta(BaseCoreProfile.Meta):
        db_table = 'accelerator_entrepreneurprofile'
        abstract = True
