# MIT License
# Copyright (c) 2017 MassChallenge, Inc.


from django.test import TestCase

from .factories import (
    ObserverFactory,
)


class TestObserver(TestCase):

    def test_str(self):
        observer = ObserverFactory()
        assert observer.email in str(observer)

    def test_str_no_first_name(self):
        observer = ObserverFactory(first_name=None)
        assert observer.email in str(observer)
