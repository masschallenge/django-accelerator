from __future__ import unicode_literals
import swapper

from django.db.models import (
    CharField,
    FloatField,
    ForeignKey,
    IntegerField,
    CASCADE,
)

from accelerator_abstract.models.accelerator_model import AcceleratorModel


class BaseCriterionOptionSpec(AcceleratorModel):
    DEFAULT_COUNT = 1
    DEFAULT_WEIGHT = 1.0

    option = CharField(max_length=64, blank=True)
    count = IntegerField(default=DEFAULT_COUNT)
    weight = FloatField(default=DEFAULT_WEIGHT)
    criterion = ForeignKey(swapper.get_model_name(
        AcceleratorModel.Meta.app_label,
        "Criterion"),
        on_delete=CASCADE)

    class Meta(AcceleratorModel.Meta):
        abstract = True
        db_table = 'accelerator_criterionoptionspec'
        verbose_name = "Application Allocator Criterion Option"

    def __str__(self):
        return "CriterionOptionSpec: %s: %s" % (self.criterion.name,
                                                self.option)
