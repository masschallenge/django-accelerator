from sorl.thumbnail import ImageField
from django.db import models
from accelerator_abstract.models.accelerator_model import AcceleratorModel
IMAGE_HELP_TEXT = ('Any png or jpg up to '
                   '2MB.Ideal dimensions: 300 x 227 pixels')
LOGO_HELP_TEXT = ('Any circle cropped png or jpg up '
                  'to 2MB.Ideal dimensions: 50 x 50 pixels')


class BaseCommunity(AcceleratorModel):
    name = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    icon = ImageField(
        upload_to='community_icon',
        verbose_name="Icon",
        help_text=LOGO_HELP_TEXT)
    image = ImageField(
        upload_to='community_image',
        verbose_name="Image",
        help_text=IMAGE_HELP_TEXT)
    assignment_order = models.PositiveIntegerField()
    is_visible = models.BooleanField(default=False)
    is_default = models.BooleanField(default=False)

    class Meta(AcceleratorModel.Meta):
        abstract = True
        verbose_name = "Community"

    def __str__(self):
        return "Community: %s" % self.name
