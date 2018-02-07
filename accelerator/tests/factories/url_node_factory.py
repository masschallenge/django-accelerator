from factory import (
    DjangoModelFactory,
    Sequence,
    SubFactory,
)
from fluent_pages.models import UrlNode

from accelerator.tests.factories import (
    MemberFactory,
)


class UrlNodeFactory(DjangoModelFactory):
    class Meta:
        model = UrlNode

    override_url = Sequence(lambda n: "/node{}/".format(n))
    author = SubFactory(MemberFactory
                        )
    title = Sequence(lambda n: "Url Node {}".format(n))
