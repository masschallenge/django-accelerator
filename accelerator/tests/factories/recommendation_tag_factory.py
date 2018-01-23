# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from factory import (
    DjangoModelFactory,
    Sequence,
)

import swapper

RecommendationTag = swapper.load_model("accelerator", "RecommendationTag")


class RecommendationTagFactory(DjangoModelFactory):

    class Meta:
        model = RecommendationTag

    text = Sequence(lambda n: "tag_{0}".format(n))
