# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from factory import (
    DjangoModelFactory,
    Sequence,
    SubFactory,
)

from accelerator.models.section import Section
from accelerator.tests.factories import NewsletterFactory
from accelerator_abstract.models.base_section import INCLUDE_FOR_CHOICES


class SectionFactory(DjangoModelFactory):
    class Meta:
        model = Section

    heading = Sequence(lambda n: "Heading text {0}".format(n))
    body = Sequence(lambda n: "Newsletter Body {0}".format(n))
    include_for = INCLUDE_FOR_CHOICES[0][0]
    newsletter = SubFactory(NewsletterFactory)
    sequence = Sequence(lambda x: x)
