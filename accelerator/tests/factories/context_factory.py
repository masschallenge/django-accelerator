import factory
from accelerator.tests.factories import IndustryFactory


class ContextObj(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class BaseContextFactory(factory.Factory):
    class Meta:
        model = ContextObj
        abstract = True


class LeafContextFactory(BaseContextFactory):
    foo = "foo"
    bar = "bar"
    industry = factory.SubFactory(IndustryFactory)


class RootContextFactory(BaseContextFactory):
    left = factory.SubFactory(LeafContextFactory)
    right = factory.SubFactory(LeafContextFactory)

