from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories import ApplicationFactory


class TestApplication(TestCase):
    def test_application_str_function(self):
        app = ApplicationFactory()
        expected_str = '%s for %s by %s' % (app.application_type.name,
                                            app.cycle.name,
                                            app.startup.name)
        assert str(app) == expected_str
