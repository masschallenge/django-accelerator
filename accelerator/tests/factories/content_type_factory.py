# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.contrib.contenttypes.models import ContentType
from factory import (
    DjangoModelFactory,
    Sequence,
)


class ContentTypeFactory(DjangoModelFactory):
    class Meta:
        model = ContentType

    app_label = "mc"
    model = Sequence(lambda n: "test_contenttypemodel{0}".format(n))
