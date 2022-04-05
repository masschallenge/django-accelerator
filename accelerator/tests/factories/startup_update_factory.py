from factory import SubFactory
from factory.django import DjangoModelFactory

from accelerator.tests.factories import (
    EntrepreneurFactory,
    StartupFactory
)
from accelerator.models import StartupUpdate


class StartupUpdateFactory(DjangoModelFactory):
    class Meta:
        model = StartupUpdate

    startup = SubFactory(StartupFactory)
    user = SubFactory(EntrepreneurFactory)
    current_status_new_name = 'new name'
    company_disposition = 'active'
    active_annualized_revenue = 2.4
    active_headcount = 3
    active_total_funding = 6.7
    active_most_recent_investment_date = "01/2022"
    active_valuation = 2.8
    ipo_valuation = 1.6
    ipo_date = "01/2022"
    acquired_valuation = 9.0
    acquired_date = "01/2022"
