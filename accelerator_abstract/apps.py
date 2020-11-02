# MIT License
# Copyright (c) 2017 MassChallenge, Inc.
import swapper
from django.apps import AppConfig
from django.contrib.auth import get_user_model


def add_get_profile_to_user_class():
    User = get_user_model()
    BaseProfile = swapper.load_model('accelerator', 'BaseProfile')
    User.add_to_class('get_profile',
                      lambda user: BaseProfile.objects.get(
                          email=user.email))


class AcceleratorAbstractConfig(AppConfig):
    name = 'accelerator_abstract'
