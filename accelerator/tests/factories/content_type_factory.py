from django.contrib.contenttypes.models import ContentType
from factory import (
    DjangoModelFactory,
    Sequence,
)


class ContentTypeFactory(DjangoModelFactory):
    class Meta:
        model = ContentType

    name = Sequence(lambda n: "test_contenttype{0}".format(n))
    app_label = "mc"
    model = Sequence(lambda n: "test_contenttypemodel{0}".format(n))
