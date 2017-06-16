#!/usr/bin/env python
import os
import sys

import django

from django.conf import settings
from shared_settings import DEFAULT_SETTINGS


def run(*args):
    if not settings.configured:
        settings.configure(**DEFAULT_SETTINGS)

    django.setup()

    parent = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, parent)

    django.core.management.call_command(
        "makemigrations",
        "accelerator",
        *args
    )


if __name__ == "__main__":
    run(*sys.argv[1:])
