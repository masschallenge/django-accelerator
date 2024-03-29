from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.test import TestCase
from django.test.client import RequestFactory
from .factories.user_factory import UserFactory
from simpleuser.email_model_backend import (
    EmailModelBackend,
)
User = get_user_model()

BAD_EMAIL = "nosuch@user.com"
BAD_PASSWORD = "bad password"
GOOD_PASSWORD = "good password"


class TestEmailModelBackend(TestCase):
    def test_authenticate_with_email(self):
        backend = EmailModelBackend()
        password = GOOD_PASSWORD
        user = UserFactory(password=make_password(password))
        assert user == backend.authenticate(request=RequestFactory(),
                                            email=user.email,
                                            password=password)

    def test_authenticate_with_username(self):
        backend = EmailModelBackend()
        password = GOOD_PASSWORD
        user = UserFactory(password=make_password(password))
        assert user == backend.authenticate(request=RequestFactory(),
                                            username=user.email,
                                            password=password)

    def test_authenticate_with_bad_password(self):
        backend = EmailModelBackend()
        password = GOOD_PASSWORD
        user = UserFactory(password=password)
        assert backend.authenticate(request=RequestFactory(),
                                    username=user.email,
                                    password=BAD_PASSWORD) is None

    def test_authenticate_with_no_user(self):
        backend = EmailModelBackend()
        assert backend.authenticate(request=RequestFactory(),
                                    email=BAD_EMAIL,
                                    password=BAD_PASSWORD) is None

    def test_get_user(self):
        backend = EmailModelBackend()
        user = UserFactory()
        assert user == backend.get_user(user.id)

    def test_get_user_for_deleted_user(self):
        backend = EmailModelBackend()
        user = UserFactory()
        id = user.id
        user.delete()
        assert backend.get_user(id) is None
