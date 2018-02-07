# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from factory import (
    DjangoModelFactory,
    Sequence,
    SubFactory,
)

from accelerator.models.application_type import ApplicationType
from accelerator.tests.factories.startup_label_factory import StartupLabelFactory


class ApplicationTypeFactory(DjangoModelFactory):
    class Meta:
        model = ApplicationType

    name = Sequence(lambda n: "Application Type {0}".format(n))
    description = Sequence(lambda n:
                           "Application Type Description {0}".format(n))
    submission_label = SubFactory(StartupLabelFactory)
