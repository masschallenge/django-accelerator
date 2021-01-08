from __future__ import unicode_literals


from accelerator_abstract.models.base_location import BaseLocation


class Location(BaseLocation):
    class Meta(BaseLocation.Meta):
        swappable = False
