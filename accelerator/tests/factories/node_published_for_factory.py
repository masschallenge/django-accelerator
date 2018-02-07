import swapper
from factory import (
    DjangoModelFactory,
    SubFactory,
)

from accelerator.apps import AcceleratorConfig
from accelerator.tests.factories.url_node_factory import UrlNodeFactory
from accelerator.tests.factories.program_role_factory import ProgramRoleFactory

NodePublishedFor = swapper.load_model(AcceleratorConfig.name,
                                      'NodePublishedFor')


class NodePublishedForFactory(DjangoModelFactory):
    class Meta:
        model = NodePublishedFor

    node = SubFactory(UrlNodeFactory)
    published_for = SubFactory(ProgramRoleFactory)
