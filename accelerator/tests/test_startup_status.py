from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import StartupStatusFactory


class TestStartupStatus(TestCase):
    def test_str(self):
        startup_status = StartupStatusFactory()
        assert startup_status.startup.name in str(startup_status)
        assert startup_status.program_startup_status.startup_status in str(
            startup_status)

    def test_can_delete_startup_status_with_no_startup_role(self):
        status = StartupStatusFactory(
            program_startup_status__startup_role=None)
        status.delete()
