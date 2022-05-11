import swapper
from django.db import models
from django.conf import settings

from accelerator_abstract.models.accelerator_model import AcceleratorModel
ACTIVE = 'active'
CLOSED_IPO = 'closed-ipo'
CLOSED_ACQUISITION = 'closed-acquisition'
CLOSED_INACTIVE = 'closed-inactive'
DEPARTED_STAFF = 'departed-staff'
USD = 'USD'
GBP = 'GBP'
EUR = 'EUR'
JPY = 'JPY'
AUD = 'AUD'
CAD = 'CAD'
CHF = 'CHF'
NZD = 'NZD'
NGN = 'NGN'
MXN = 'MXN'

CURRENCY_CHOICES = [
    (USD, USD), (GBP, GBP),
    (EUR, EUR), (JPY, JPY),
    (AUD, AUD), (CAD, CAD),
    (CHF, CHF), (NZD, NZD),
    (NGN, NGN), (MXN, MXN),
]
COMPANY_DISPOSITION_CHOICES = (
    (ACTIVE, ACTIVE),
    (CLOSED_IPO, CLOSED_IPO),
    (CLOSED_ACQUISITION, CLOSED_ACQUISITION),
    (CLOSED_INACTIVE, CLOSED_INACTIVE),
    (DEPARTED_STAFF, DEPARTED_STAFF),
)

DISCLOSURE_CONSENT = (
    'I consent to allow Mass Challenge'
    ' to disclose current funding status')


class BaseStartupUpdate(AcceleratorModel):
    startup = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "Startup"),
        on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    current_status_hiring = models.BooleanField(
        verbose_name='This company is currently hiring',
        default=False)
    current_status_seeking_investors = models.BooleanField(
        verbose_name='This company is currently seeking investors',
        default=False)
    funding_disclosure_consent = models.BooleanField(
        verbose_name=DISCLOSURE_CONSENT,
        default=False)
    current_status_name_change = models.BooleanField(
        verbose_name='This company has changed its name',
        default=False)
    current_status_new_name = models.TextField(
        blank=True,
        null=True,
        verbose_name='Current status name')
    company_disposition = models.CharField(
        max_length=100,
        verbose_name='Company disposition',
        choices=COMPANY_DISPOSITION_CHOICES)
    active_annualized_revenue = models.DecimalField(
        verbose_name='Annualized revenue',
        max_digits=13,
        blank=True,
        null=True,
        decimal_places=2)
    active_annualized_revenue_usd = models.DecimalField(
        verbose_name='Annualized revenue (in US dollars)',
        max_digits=13,
        blank=True,
        null=True,
        decimal_places=2)
    active_headcount = models.IntegerField(
        blank=True,
        null=True,
        verbose_name='Headcount (Full Time, Part-Time, and Volunteers)')
    active_total_funding = models.DecimalField(
        verbose_name='Total Funding Raised',
        blank=True,
        null=True,
        max_digits=13,
        decimal_places=2)
    active_total_funding_usd = models.DecimalField(
        verbose_name='Total Funding Raised (in US dollars)',
        blank=True,
        null=True,
        max_digits=13,
        decimal_places=2)
    active_funding_source_founders = models.BooleanField(
        verbose_name='Founder',
        default=False)
    active_funding_source_friends = models.BooleanField(
        verbose_name='Friends and Family',
        default=False)
    active_funding_source_angel = models.BooleanField(
        verbose_name='Angel',
        default=False)
    active_funding_source_venture = models.BooleanField(
        verbose_name='Institutional VC',
        default=False)
    active_funding_source_private_equity = models.BooleanField(
        verbose_name='Private Equity',
        default=False)
    active_funding_source_gifts_grants = models.BooleanField(
        verbose_name='Gifts',
        default=False)
    active_funding_source_other = models.BooleanField(
        verbose_name='Active funding source other',
        default=False)
    active_most_recent_investment_date = models.DateField(
        blank=True,
        null=True,
        verbose_name='Date of most recent investment')
    active_valuation = models.DecimalField(
        blank=True,
        null=True,
        verbose_name='Valuation',
        max_digits=13,
        decimal_places=2)
    active_valuation_usd = models.DecimalField(
        blank=True,
        null=True,
        verbose_name='Valuation (in US dollars)',
        max_digits=13,
        decimal_places=2)
    ipo_valuation = models.DecimalField(
        verbose_name='Valuation',
        blank=True,
        null=True,
        max_digits=13,
        decimal_places=2)
    ipo_valuation_usd = models.DecimalField(
        verbose_name='Valuation (in US dollars)',
        blank=True,
        null=True,
        max_digits=13,
        decimal_places=2)
    ipo_date = models.DateField(
        blank=True,
        null=True,
        verbose_name='Date')
    acquired_valuation = models.DecimalField(
        verbose_name='Valuation',
        blank=True,
        null=True,
        max_digits=13,
        decimal_places=2)
    acquired_valuation_usd = models.DecimalField(
        verbose_name='Valuation (in US dollars)',
        blank=True,
        null=True,
        max_digits=13,
        decimal_places=2)
    acquired_date = models.DateField(
        blank=True,
        null=True,
        verbose_name='Date')
    currency_type = models.CharField(
        verbose_name='Status Currency',
        max_length=5,
        choices=CURRENCY_CHOICES,
        default=USD)

    class Meta(AcceleratorModel.Meta):
        abstract = True

    def __str__(self):
        return self.startup.organization.name
