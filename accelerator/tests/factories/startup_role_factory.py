# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from factory import Sequence
from factory.django import DjangoModelFactory

from accelerator.models import StartupRole


class StartupRoleFactory(DjangoModelFactory):
    class Meta:
        model = StartupRole

    name = Sequence(lambda x: "StartupRole %d" % x)
