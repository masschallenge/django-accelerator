from __future__ import unicode_literals

from datetime import (
    datetime,
    timedelta,
)

import swapper
from factory import SubFactory
from factory.django import DjangoModelFactory
from pytz import utc

from accelerator.models import (
    STALE_NOSTARTUP_BUCKET_TYPE,
    STALE_LEADS_GROUP,
)
from accelerator.tests.factories.program_cycle_factory import (
    ProgramCycleFactory
)
from accelerator.tests.factories.program_factory import ProgramFactory
from accelerator.tests.factories.program_role_factory import ProgramRoleFactory

BucketState = swapper.load_model('accelerator', 'BucketState')


class BucketStateFactory(DjangoModelFactory):
    class Meta:
        model = BucketState

    basis = BucketState.CYCLE_BASED
    name = STALE_NOSTARTUP_BUCKET_TYPE
    group = STALE_LEADS_GROUP
    sort_order = 1
    cycle = SubFactory(ProgramCycleFactory)
    program = SubFactory(ProgramFactory)
    last_update = utc.localize(datetime.now() - timedelta(1))
    program_role = SubFactory(ProgramRoleFactory)
