# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from accelerator.tests.factories import StartupStatusFactory


def test_can_delete_startup_status_with_no_startup_role():
    status = StartupStatusFactory(
        program_startup_status__startup_role=None)
    status.delete()
