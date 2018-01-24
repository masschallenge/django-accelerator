# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper


from django.conf import settings
from accelerator_abstract.models.base_application import (
    APPLICATION_STATUSES,
    BaseApplication,
    COMPLETE_APP_STATUS,
    DELAYED_STATUS,
    INCOMPLETE_APP_STATUS,
    INSTANT_STATUS,
    PAYMENT_STATUSES,
    REFUND_STATUSES,
    SUBMITTED_APP_STATUS,
)


class Application(BaseApplication):
    class Meta(BaseApplication.Meta):
        swappable = swapper.swappable_setting(
            BaseApplication.Meta.app_label, 'Application')
