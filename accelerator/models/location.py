from __future__ import unicode_literals

import swapper

from accelerator_abstract.models.base_location import BaseLocation


class Location(BaseLocation):
    class Meta(BaseLocation.Meta):
        swappable = swapper.swappable_setting(
            BaseLocation.Meta.app_label, "Location")
