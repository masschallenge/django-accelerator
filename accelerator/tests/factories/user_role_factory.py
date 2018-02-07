import swapper
from factory import (
    DjangoModelFactory,
    Sequence,
)

from accelerator.apps import AcceleratorConfig

UserRole = swapper.load_model(AcceleratorConfig.name, 'UserRole')


class UserRoleFactory(DjangoModelFactory):
    class Meta:
        model = UserRole

    name = Sequence(lambda n: "User Role {0}".format(n))
    url_slug = Sequence(lambda n: "role_{0}".format(n))
    sort_order = Sequence(lambda n: n)
