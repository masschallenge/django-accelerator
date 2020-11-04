# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from django.conf import settings
from django.core.validators import EmailValidator
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from accelerator_abstract.models.accelerator_model import AcceleratorModel


@python_2_unicode_compatible
class BaseReference(AcceleratorModel):
    application = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "Application"),
        on_delete=models.CASCADE)
    email = models.CharField(verbose_name="Email address",
                             max_length=100,
                             validators=[EmailValidator()])
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    reference_hash = models.CharField(max_length=50, unique=True)
    sent = models.DateTimeField(blank=True, null=True)
    accessed = models.DateTimeField(blank=True, null=True)
    submitted = models.DateTimeField(blank=True, null=True)
    confirmed_first_name = models.CharField(max_length=50, blank=True)
    confirmed_last_name = models.CharField(max_length=50, blank=True)
    confirmed_company = models.CharField(max_length=50, blank=True)
    question_1_rating = models.IntegerField(null=True)
    question_2_rating = models.IntegerField(null=True)
    comments = models.TextField(blank=True)
    requesting_user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
                                        on_delete=models.CASCADE)

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_reference'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True

    def __str__(self):
        if self.submitted:
            return "Reference for %s from %s" % (self.application, self.email)
        else:
            return ("Reference request for %s to %s" %
                    (self.application, self.email))
