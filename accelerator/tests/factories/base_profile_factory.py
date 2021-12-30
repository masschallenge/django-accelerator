from __future__ import unicode_literals

import swapper
from factory import SubFactory
from factory.django import DjangoModelFactory
from simpleuser.tests.factories.user_factory import UserFactory

BaseProfile = swapper.load_model('accelerator', 'BaseProfile')


class BaseProfileFactory(DjangoModelFactory):
    class Meta:
        model = BaseProfile

    user = SubFactory(UserFactory)
    user_type = "ENTREPRENEUR"

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        model_class.objects.filter(
            user=kwargs['user'], user_type="MEMBER").delete()
        manager = cls._get_manager(model_class)
        return manager.create(*args, **kwargs)
