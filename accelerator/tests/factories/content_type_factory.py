# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.contrib.contenttypes.models import ContentType

from factory import Sequence
from factory.django import DjangoModelFactory

from accelerator.tests.utils import get_app_name


class ContentTypeFactory(DjangoModelFactory):
    class Meta:
        model = ContentType

    app_label = get_app_name()
    model = Sequence(lambda n: "test_contenttypemodel{0}".format(n))
