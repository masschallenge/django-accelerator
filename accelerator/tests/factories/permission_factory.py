from django.contrib.auth.models import Permission
from factory import (
    DjangoModelFactory,
    Sequence,
    SubFactory,
)

from accelerator.tests.factories.content_type_factory import ContentTypeFactory


class PermissionFactory(DjangoModelFactory):
    class Meta:
        model = Permission

    name = Sequence(lambda n: "test_permission{0}".format(n))
    content_type = SubFactory(ContentTypeFactory)
    codename = Sequence(lambda n: "test_permcode{0}".format(n))
