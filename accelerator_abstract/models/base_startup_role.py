from __future__ import unicode_literals

from django.db.models import CharField

from accelerator_abstract.models.accelerator_model import AcceleratorModel


class BaseStartupRole(AcceleratorModel):
    # Known Startup Roles
    FINALIST = "Finalist"
    ENTRANT = "Entrant"
    FAST_TRACK = "Fast Track"
    AIR = "Alum In Residence"
    MC_STAFF = "MC Staff"
    WINNER = "Winner"
    GOLD_WINNER = "Gold Winner"
    SILVER_WINNER = "Silver Winner"
    PLATINUM_WINNER = "Platinum Winner"
    DIAMOND_WINNER = "Diamond Winner"
    IN_KIND_WINNER = "In-Kind Winner"
    SIDECAR_WINNER = "Sidecar Winner"
    ALUM = "Alum"

    FINALIST_STARTUP_ROLES = [FINALIST,
                              AIR,
                              MC_STAFF]

    WINNER_STARTUP_ROLES = [WINNER,
                            GOLD_WINNER,
                            SILVER_WINNER,
                            PLATINUM_WINNER,
                            DIAMOND_WINNER,
                            IN_KIND_WINNER,
                            SILVER_WINNER]

    name = CharField(max_length=255)

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_startuprole'
        abstract = True

    def __str__(self):
        return self.name
