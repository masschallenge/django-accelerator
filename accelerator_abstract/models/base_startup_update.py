import swapper
from django.db import models
from django.conf import settings

from accelerator_abstract.models.accelerator_model import AcceleratorModel
ACTIVE = 'active'
CLOSED_IPO = 'closed-ipo'
CLOSED_ACQUISITION = 'closed-acquisition'
CLOSED_INACTIVE = 'closed-inactive'
DEPARTED_STAFF = 'departed-staff'

COMPANY_DISPOSITION_CHOICES = (
    (ACTIVE, ACTIVE),
    (CLOSED_IPO, CLOSED_IPO),
    (CLOSED_ACQUISITION, CLOSED_ACQUISITION),
    (CLOSED_INACTIVE, CLOSED_INACTIVE),
    (DEPARTED_STAFF, DEPARTED_STAFF),
)


class BaseStartupUpdate(AcceleratorModel):
    startup = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "Startup"),
        on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    current_status_hiring = models.BooleanField(
        verbose_name='Current status hiring',
        default=False)
    current_status_seeking_investors = models.BooleanField(
        verbose_name='Current status seeeking investors',
        default=False)
    funding_disclosure_consent = models.BooleanField(
        verbose_name='Funding disclosure consent',
        default=False)
    current_status_name_change = models.BooleanField(
        verbose_name='Current status name change',
        default=False)
    current_status_new_name = models.TextField(
        verbose_name='Current status name')
    company_disposition = models.CharField(
        max_length=100,
        verbose_name='Company disposition',
        choices=COMPANY_DISPOSITION_CHOICES)
    active_annualized_revenue = models.DecimalField(
        verbose_name='Active annualized revenue',
        max_digits=13,
        decimal_places=2)
    active_headcount = models.IntegerField(
        verbose_name='Active headcount')
    active_total_funding = models.DecimalField(
        verbose_name='Active total funding',
        max_digits=13,
        decimal_places=2)
    active_funding_source_founders = models.BooleanField(
        verbose_name='Active funding source founders',
        default=False)
    active_funding_source_friends = models.BooleanField(
        verbose_name='Active funding source friends',
        default=False)
    active_funding_source_angel = models.BooleanField(
        verbose_name='Active funding source angel',
        default=False)
    active_funding_source_venture = models.BooleanField(
        verbose_name='Active funding source venture',
        default=False)
    active_funding_source_private_equity = models.BooleanField(
        verbose_name='Active funding source private equity',
        default=False)
    active_funding_source_gifts_grants = models.BooleanField(
        verbose_name='Active funding source gift grants',
        default=False)
    active_funding_source_other = models.BooleanField(
        verbose_name='Active funding source other',
        default=False)
    active_most_recent_investment_date = models.DateField(
        verbose_name='Active most recent investment date')
    active_valuation = models.DecimalField(
        verbose_name='Active valuation',
        max_digits=13,
        decimal_places=2)
    ipo_valuation = models.DecimalField(
        verbose_name='IPO valuation',
        max_digits=13,
        decimal_places=2)
    ipo_date = models.DateField(verbose_name='IPO date')
    acquired_valuation = models.DecimalField(
        verbose_name='Acquired valuation',
        max_digits=13,
        decimal_places=2)
    acquired_date = models.DateField(verbose_name='Acquired date')

    class Meta(AcceleratorModel.Meta):
        abstract = True

    def __str__(self):
        return self.startup.organization.name
