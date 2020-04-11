# MIT License
# Copyright (c) 2017 MassChallenge, Inc.


# Though this class is (for now) still with other models, it is essentially
# just a collection of string constants. It is not a Django model. See AC-6679
class StartupRole:
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
