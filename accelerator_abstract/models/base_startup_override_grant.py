# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import swapper

from accelerator_abstract.models.accelerator_model import AcceleratorModel
from django.db import models


@python_2_unicode_compatible
class BaseStartupOverrideGrant(AcceleratorModel):
    startup = models.ForeignKey(swapper.get_model_name(AcceleratorModel.Meta.app_label, "Startup"))
    program_override = models.ForeignKey(swapper.get_model_name(AcceleratorModel.Meta.app_label, "ProgramOverride"))

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_startupoverridegrant'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True
        verbose_name_plural = 'Startup Override Grants'

    def __str__(self):
        return ("Override grant (%s) for %s for %s" %
                (self.program_override.name,
                 self.startup.name,
                 self.program_override.program.name))
