import swapper
from factory import (
    DjangoModelFactory,
    Sequence,
)

from accelerator.apps import AcceleratorConfig
from accelerator.models import MIGRATION_STATUS_OLD

ModelChange = swapper.load_model(AcceleratorConfig.name, 'ModelChange')


class ModelChangeFactory(DjangoModelFactory):
    class Meta:
        model = ModelChange
        django_get_or_create = ('name',)

    name = Sequence(lambda n: "Model Change {}".format(n))
    status = MIGRATION_STATUS_OLD
