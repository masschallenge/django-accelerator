import swapper
from django.db import models

from accelerator_abstract.models.accelerator_model import AcceleratorModel

EXCLUDED_FIELDS = ['id', 'created_at', 'updated_at', 'startup', 'applications']

PAIN_POINT_HELP_TEXT = ('Please describe what '
                        'problem you are trying to solve?')
SOLUTION_HELP_TEXT = ('What is innovative about '
                      'your solution, technology, business model etc?')
IMPACT_HELP_TEXT = ('Define the 1 year and 5 '
                    'year impact that you hope to accomplish')
MARKET_HELP_TEXT = ('How would you define your potential market '
                    'and what is the total addressable market size?')
VALUE_PROPOSITION_HELP_TEXT = ('What will be your messaging to users & '
                               'customers and how do you plan to spread'
                               ' that message?')
SALES_HELP_TEXT = ('Which channels will you likely reach '
                   'your customers/users through?')
COMPETITORS_HELP_TEXT = ('Which organizations compete with'
                         ' your current value offering and who might '
                         'do so in the future?')
PRODUCT_COMPLEMENT_HELP_TEXT = ('Which organizations and/or products'
                                ' complement your offering in the'
                                ' market? Do you know of and/or '
                                'anticipate any value chain partners?')
PRIMARY_ADVANTAGE_HELP_TEXT = ('What are your primary advantages'
                               ' relative to existing or potential'
                               ' competitors? Why will you win?')
DRIVER_HELP_TEXT = ('What are the key drivers of '
                    'business economics (price points, margins, etc)?')
INTELLECTUAL_PROPERTY_HELP_TEXT = ('What IP (Intellectual Property) exist'
                                   ' for your business or in your industry?')
REGULATORY_HELP_TEXT = ('What regulatory requirements exist '
                        'for your business or in your industry?')
TEAM_SUMMARY_HELP_TEXT = ('Please share some background information '
                          'on your team members and tell us what makes'
                          ' your team special.')
INVESTORS_HELP_TEXT = ('Please tell us about current or '
                       'anticipated advisors and investors.')
VALIDATION_HELP_TEXT = ('What traction have you made to '
                        'date with market validation?')


class BaseBusinessProposition(AcceleratorModel):
    startup = models.ForeignKey(
        swapper.get_model_name('accelerator', 'Startup'),
        related_name='business_propositions',
        on_delete=models.CASCADE)
    pain_point = models.TextField(blank=True,
                                  null=True,
                                  help_text=PAIN_POINT_HELP_TEXT,
                                  verbose_name="Customer Pain Point")
    solution = models.TextField(blank=True,
                                null=True,
                                help_text=SOLUTION_HELP_TEXT,
                                verbose_name='Solution')
    impact = models.TextField(blank=True,
                              null=True,
                              help_text=IMPACT_HELP_TEXT,
                              verbose_name='One-Year / Five-Year Impact')
    market = models.TextField(
        blank=True,
        null=True,
        help_text=MARKET_HELP_TEXT,
        verbose_name='Potential Market / Addressable Size')
    value_proposition = models.TextField(
        blank=True,
        null=True,
        help_text=VALUE_PROPOSITION_HELP_TEXT,
        verbose_name='Value Proposition / Marketing Message')
    sales = models.TextField(
        blank=True,
        null=True,
        help_text=SALES_HELP_TEXT,
        verbose_name='Sales and Distribution / Channels')
    competitors = models.TextField(
        blank=True,
        null=True,
        help_text=COMPETITORS_HELP_TEXT,
        verbose_name='Current and Future Competitors')
    product_complements = models.TextField(
        blank=True,
        null=True,
        help_text=PRODUCT_COMPLEMENT_HELP_TEXT,
        verbose_name='Product Complements / Value Chain Partners')
    primary_advantages = models.TextField(
        blank=True,
        null=True,
        help_text=PRIMARY_ADVANTAGE_HELP_TEXT,
        verbose_name='Primary Advantages vs Competitors')
    drivers = models.TextField(
        blank=True,
        null=True,
        help_text=DRIVER_HELP_TEXT,
        verbose_name='Key Drivers of Business Economics')
    intellectual_property = models.TextField(
        blank=True,
        null=True,
        help_text=INTELLECTUAL_PROPERTY_HELP_TEXT,
        verbose_name='Intellectual Property')
    regulation = models.TextField(
        blank=True,
        null=True,
        help_text=REGULATORY_HELP_TEXT,
        verbose_name='Regulatory Requirements')
    team_summary = models.TextField(
        blank=True,
        null=True,
        help_text=TEAM_SUMMARY_HELP_TEXT,
        verbose_name='Team (Backgrounds, advantages)')
    investors = models.TextField(
        blank=True,
        null=True,
        help_text=INVESTORS_HELP_TEXT,
        verbose_name='Current or anticipated advisors or investors')
    validation = models.TextField(
        blank=True,
        null=True,
        help_text=VALIDATION_HELP_TEXT,
        verbose_name='Traction and Market Validation')

    class Meta(AcceleratorModel.Meta):
        abstract = True

    def __str__(self):
        return self.startup.organization.name

    def complete(self):
        fields = self._meta.get_fields(include_parents=False)
        for field in fields:
            is_text_field = field.name not in EXCLUDED_FIELDS
            value = getattr(self, field.name)
            if is_text_field and (not value or len(value) < 20):
                return False
        return True
