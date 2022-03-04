import swapper
from django.db import models

from accelerator_abstract.models.accelerator_model import AcceleratorModel

EXCLUDED_FIELDS = ['id', 'created_at', 'updated_at', 'startup']


class BaseBusinessProposition(AcceleratorModel):
    startup = models.ForeignKey(
        swapper.get_model_name('accelerator', 'Startup'),
        on_delete=models.CASCADE)
    pain_point = models.TextField(blank=True,
                                  null=True,
                                  verbose_name="Customer Pain Point")
    solution = models.TextField(blank=True,
                                null=True,
                                verbose_name='Solution')
    impact = models.TextField(blank=True,
                              null=True,
                              verbose_name='One-Year / Five-Year Impact (?)')
    market = models.TextField(
        blank=True,
        null=True,
        verbose_name='Potential Market / Addressable Size')
    value_proposition = models.TextField(
        blank=True,
        null=True,
        verbose_name='Value Proposition / Marketing Message')
    sales = models.TextField(
        blank=True,
        null=True,
        verbose_name='Sales and Distribution / Channels')
    competitors = models.TextField(
        blank=True,
        null=True,
        verbose_name='Current and Future Competitors')
    product_complements = models.TextField(
        blank=True,
        null=True,
        verbose_name='Product Complements / Value Chain Partners')
    primary_advantages = models.TextField(
        blank=True,
        null=True,
        verbose_name='Primary Advantages vs Competitors')
    drivers = models.TextField(
        blank=True,
        null=True,
        verbose_name='Key Drivers of Business Economics')
    intellectual_property = models.TextField(
        blank=True,
        null=True,
        verbose_name='Intellectual Property')
    regulation = models.TextField(
        blank=True,
        null=True,
        verbose_name='Regulatory Requirements')
    team_summary = models.TextField(
        blank=True,
        null=True,
        verbose_name='Team (Backgrounds, advantages)')
    investors = models.TextField(
        blank=True,
        null=True,
        verbose_name='Current or anticipated advisors or investors')
    validation = models.TextField(
        blank=True,
        null=True,
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
