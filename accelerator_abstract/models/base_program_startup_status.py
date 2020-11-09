# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from sorl.thumbnail import ImageField

from accelerator_abstract.models.accelerator_model import AcceleratorModel

BADGE_NONE = "NONE"
BADGE_STARTUP_LIST = "STARTUP_LIST"
BADGE_STARTUP_PROFILE = "STARTUP_PROFILE"
BADGE_STARTUP_LIST_AND_PROFILE = "STARTUP_LIST_AND_PROFILE"

STARTUP_BADGE_DISPLAY_VALUES = (
    (BADGE_NONE, 'None'),
    (BADGE_STARTUP_LIST, 'Only on startup list'),
    (BADGE_STARTUP_PROFILE, 'Only on startup profile'),
    (BADGE_STARTUP_LIST_AND_PROFILE, 'Startup list and profile'))


@python_2_unicode_compatible
class BaseProgramStartupStatus(AcceleratorModel):
    program = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "Program"),
        on_delete=models.CASCADE)
    startup_status = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    startup_role = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "StartupRole"),
        null=True,
        blank=True,
        on_delete=models.CASCADE)
    startup_list_include = models.BooleanField(
        default=False,
        help_text=("Include this startup status as a tab "
                   "in the public startup list"))
    startup_list_tab_title = models.CharField(max_length=50, null=True)
    startup_list_tab_description = models.TextField(
        max_length=1000,
        blank=True,
        help_text="You may use HTML, including links")
    startup_list_tab_id = models.CharField(
        max_length=30,
        null=True,
        help_text="The slug used in the public URL")
    startup_list_tab_order = models.IntegerField(null=True)
    include_stealth_startup_names = models.BooleanField(default=False)
    badge_image = ImageField(
        upload_to='badge_images',
        blank=True)
    badge_display = models.CharField(choices=STARTUP_BADGE_DISPLAY_VALUES,
                                     max_length=30, default=BADGE_NONE)
    status_group = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Only one status is shown from the same status group; "
                  "which one is determined by sort order")
    sort_order = models.IntegerField(
        blank=True,
        null=True,
        help_text="Order")

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_programstartupstatus'
        abstract = True
        verbose_name_plural = 'Program Startup Statuses'
        ordering = ['program', 'sort_order', 'startup_status']

    def __str__(self):
        return "%s (Program Startup Status for %s)" % (self.startup_status,
                                                       self.program)
