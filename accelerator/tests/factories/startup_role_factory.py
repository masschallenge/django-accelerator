# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import Sequence
from factory.django import DjangoModelFactory

from accelerator.apps import AcceleratorConfig

StartupRole = swapper.load_model(AcceleratorConfig.name, 'StartupRole')


class StartupRoleFactory(DjangoModelFactory):
    class Meta:
        model = StartupRole

    name = Sequence(lambda x: "StartupRole %d" % x)
