from accelerator.models.core_profile import CoreProfile
from accelerator.tests.factories import CoreProfileFactory
from factory import SubFactory

from accelerator.tests.factories.industry_factory import IndustryFactory
from accelerator.tests.factories.expert_category_factory import (
    ExpertCategoryFactory
)


class CoreProfileModelFactory(CoreProfileFactory):
    expert_category = SubFactory(ExpertCategoryFactory)
    primary_industry = SubFactory(IndustryFactory)

    class Meta:
        model = CoreProfile
