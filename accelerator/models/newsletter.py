# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals


from accelerator_abstract.models import BaseNewsletter


class Newsletter(BaseNewsletter):
    class Meta(BaseNewsletter.Meta):
        swappable = False
