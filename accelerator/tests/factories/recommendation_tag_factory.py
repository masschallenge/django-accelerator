# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from factory import Sequence
from factory.django import DjangoModelFactory

from accelerator.models import RecommendationTag


class RecommendationTagFactory(DjangoModelFactory):
    class Meta:
        model = RecommendationTag

    text = Sequence(lambda n: "tag_{0}".format(n))
