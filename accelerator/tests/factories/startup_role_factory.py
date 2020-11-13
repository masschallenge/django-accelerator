# MIT License
# Copyright (c) 2017 MassChallenge, Inc.


import swapper
from factory import Sequence
from factory.django import DjangoModelFactory

StartupRole = swapper.load_model('accelerator', 'StartupRole')


class StartupRoleFactory(DjangoModelFactory):
    class Meta:
        model = StartupRole

    name = Sequence(lambda x: "StartupRole %d" % x)
