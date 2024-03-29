from __future__ import unicode_literals

from django.core.validators import RegexValidator
from django.db import models
from django.template.defaultfilters import slugify

from accelerator_abstract.models.accelerator_model import AcceleratorModel

STARTUP_TYPE = "startup"
PARTNER_TYPE = "partner"


class BaseOrganization(AcceleratorModel):
    name = models.CharField(max_length=255)
    website_url = models.URLField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Website URL")
    twitter_handle = models.CharField(
        max_length=40,
        blank=True,
        null=True,
        help_text='Omit the "@". We\'ll add it.',
        verbose_name="Twitter handle")
    public_inquiry_email = models.EmailField(verbose_name="Email address",
                                             max_length=100,
                                             blank=True, null=True)
    url_slug = models.CharField(
        max_length=64,
        blank=True,
        null=True,
        default="",  # This actually gets replaced by a real slug.
        unique=True,
        validators=[
            RegexValidator(regex=r"^[\w-]+$",
                           message="Letters, numbers, and dashes only.")
        ]
    )
    current_status_hiring = models.BooleanField(
        verbose_name='Current status hiring',
        default=False)
    current_status_seeking_investors = models.BooleanField(
        verbose_name='Current status seeeking investors',
        default=False)
    funding_disclosure_consent = models.BooleanField(
        verbose_name='Funding disclosure consent',
        default=False)

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_organization'
        verbose_name_plural = 'Organizations'
        ordering = ['name', ]
        abstract = True

    def save(self, *args, **kwargs):
        if self.url_slug == "":
            self.url_slug = slug_from_instance(self)
        super(BaseOrganization, self).save(*args, **kwargs)


def slug_from_instance(organization):
    slug = slugify(organization.name)
    if slug == "":
        slug = "organization"
    slug = slug[:61]
    slugbase = slug
    i = 0
    while (organization._meta.model.objects.filter(
            url_slug=slug).exists() and
           (i < 100 or slugbase == "organization")):
        i += 1
        slug = slugbase + "-" + str(i)
    return slug
