# MIT License
# Copyright (c) 2017 MassChallenge, Inc.
import swapper
from django.apps import AppConfig
from django.contrib.auth import get_user_model
from accelerator.apps import AcceleratorConfig


class AcceleratorAbstractConfig(AppConfig):
    name = 'accelerator_abstract'

    def ready(self):
        User = get_user_model()
        BaseProfile = swapper.load_model(AcceleratorConfig.name, 'BaseProfile')
        User.add_to_class('get_profile',
                          lambda user: BaseProfile.objects.get(
                              email=user.email))
