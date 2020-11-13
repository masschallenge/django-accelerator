# MIT License
# Copyright (c) 2017 MassChallenge, Inc.


import swapper

from accelerator_abstract.models import BaseOrganization


class Organization(BaseOrganization):
    class Meta(BaseOrganization.Meta):
        swappable = swapper.swappable_setting(BaseOrganization.Meta.app_label,
                                              'Organization')
