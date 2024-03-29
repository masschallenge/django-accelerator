from __future__ import unicode_literals

from accelerator.tests.factories.ethno_racial_identity_factory import (
    EthnoRacialIdentityFactory,
)
from accelerator.tests.factories.expert_category_factory import (
    ExpertCategoryFactory
)
from accelerator.tests.factories.industry_factory import IndustryFactory
from accelerator.tests.factories.program_factory import ProgramFactory


def expert_data(user, password="password"):
    return {
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "title": "Some Title",
        "company": "Company",
        "expert_category": ExpertCategoryFactory().id,
        "primary_industry": IndustryFactory().id,
        "additional_industries": [IndustryFactory().id],
        "privacy_email": "public",
        "privacy_phone": "public",
        "privacy_web": "public",
        "home_program_family": ProgramFactory().program_family.id,
        "public_website_consent": True,
        "username": user.username,
        "password": password,
        "date_joined": user.date_joined.date(),
        "ethno_racial_identification": [EthnoRacialIdentityFactory().id],
    }
