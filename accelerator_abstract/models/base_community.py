from sorl.thumbnail import ImageField
from django.db import models
from accelerator_abstract.models.accelerator_model import AcceleratorModel
HELP_TEXT = 'Any png or jpg upto to 2mb. Ideal dimensions: 600 x 400 pixels'


class BaseCommunity(AcceleratorModel):
    name = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    logo = ImageField(
        upload_to='community_logo',
        verbose_name="Logo",
        help_text=HELP_TEXT)
    image = ImageField(
        upload_to='community_image',
        verbose_name="Image",
        help_text=HELP_TEXT)
    assignment_order = models.PositiveIntegerField()
    is_visible = models.BooleanField(default=False)
    is_default = models.BooleanField(default=False)

    class Meta(AcceleratorModel.Meta):
        abstract = True
        verbose_name = "Community"

    def __str__(self):
        return "Community: %s" % self.name
