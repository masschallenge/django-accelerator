# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from datetime import (
    datetime,
    timedelta,
)

import swapper
from factory import (
    Sequence,
    SubFactory,
)
from factory.django import DjangoModelFactory

from pytz import utc

from accelerator.tests.factories.startup_factory import StartupFactory

JobPosting = swapper.load_model('accelerator', 'JobPosting')


class JobPostingFactory(DjangoModelFactory):
    class Meta:
        model = JobPosting

    startup = SubFactory(StartupFactory)
    postdate = utc.localize(datetime.now() - timedelta(1))
    type = Sequence(lambda n: 'type {0}'.format(n))
    title = Sequence(lambda n: 'engineer level {0}'.format(n))
    description = 'Create mission-critical brand technologies'
    applicationemail = 'null@example.com'
    more_info_url = Sequence(lambda n: 'http://example.com/job{0}'.format(n))
