from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.test import TestCase

from .factories import (
    NewsletterFactory,
)

User = get_user_model()


class TestNewsletter(TestCase):
    def test_str(self):
        newsletter = NewsletterFactory()
        assert newsletter.name in str(newsletter)
