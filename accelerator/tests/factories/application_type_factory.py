# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import (
    DjangoModelFactory,
    Sequence,
    SubFactory,
)

from accelerator.apps import AcceleratorConfig
from accelerator.tests.factories.startup_label_factory import (
    StartupLabelFactory
)

ApplicationType = swapper.load_model(AcceleratorConfig.name, 'ApplicationType')


class ApplicationTypeFactory(DjangoModelFactory):
    class Meta:
        model = ApplicationType

    name = Sequence(lambda n: 'Application Type {0}'.format(n))
    description = Sequence(lambda n:
                           'Application Type Description {0}'.format(n))
    submission_label = SubFactory(StartupLabelFactory)
