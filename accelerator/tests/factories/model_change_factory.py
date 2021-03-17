# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import Sequence
from factory.django import DjangoModelFactory

from accelerator.models import MIGRATION_STATUS_OLD

ModelChange = swapper.load_model('accelerator', 'ModelChange')


class ModelChangeFactory(DjangoModelFactory):
    class Meta:
        model = ModelChange
        django_get_or_create = ('name',)

    name = Sequence(lambda n: "Model Change {}".format(n))
    status = MIGRATION_STATUS_OLD
