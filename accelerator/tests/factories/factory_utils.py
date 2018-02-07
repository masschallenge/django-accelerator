from accelerator.tests.factories.expert_category_factory import (
    ExpertCategoryFactory
)
from accelerator.tests.factories.industry_factory import IndustryFactory
from accelerator.tests.factories.program_factory import ProgramFactory


# Note: Not sure this is the right place for this.
# It can't go in mc.tests.utils since it depends
# on some factories_old and some of the factories_old depend
# on mc.tests.utils.  It's kind of like a context,
# but a bit different.
def expert_data(user):
    return {
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "gender": "p",
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
        "password": user.password,
        "date_joined": user.date_joined,
    }
