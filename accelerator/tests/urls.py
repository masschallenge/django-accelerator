# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

"""
This urlconf exists because Django expects ROOT_URLCONF to exist.
"""
from django.conf.urls import url

urlpatterns = [
    url('([\w]+)', lambda x: x, name='mock')
]
