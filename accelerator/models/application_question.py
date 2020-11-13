# MIT License
# Copyright (c) 2017 MassChallenge, Inc.


import swapper

from accelerator_abstract.models import BaseApplicationQuestion
from accelerator_abstract.models.accelerator_model import AcceleratorModel


class ApplicationQuestion(BaseApplicationQuestion):
    class Meta(AcceleratorModel.Meta):
        swappable = swapper.swappable_setting(
            BaseApplicationQuestion.Meta.app_label, "ApplicationQuestion")
