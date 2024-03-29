#todo: these could go in each kTelescopes
kPortionPerc = 0.25
kNumPortions = int(1 / kPortionPerc)

#telescopes
kTelescopes = {
    1: {"name": "Keck 1"},
    2: {"name": "Keck 2"}
}

#instruments
kInstruments = {
    "HIRESb":    {"telNum": 1, "doRuns": False},
    "HIRESr":    {"telNum": 1, "doRuns": False},
    "LRIS-ADC":  {"telNum": 1, "doRuns": False},
    "LRISp-ADC": {"telNum": 1, "doRuns": False},
    "MOSFIRE":   {"telNum": 1, "doRuns": False},
    "OSIRIS":    {"telNum": 1, "doRuns": False},

    "ESI":     {"telNum": 2, "doRuns": False},
    "DEIMOS":  {"telNum": 2, "doRuns": True},
    "KCWI":    {"telNum": 2, "doRuns": False},
    "NIRES":   {"telNum": 2, "doRuns": False},
    "NIRC2":   {"telNum": 2, "doRuns": False},
    "NIRSPEC": {"telNum": 2, "doRuns": False},
}

# score added for slot match with date range preference
# P = preferred, A = acceptable, N = neutral, X = avoid
# NOTE: A small non-zero score is given to X to differentiate it from slots that are absolutely not allowed.
kMoonDatePrefScore = {
    'P': 10,
    'A': 5,
    'N': 2,
    'X': 0.1
}

#Slot score percentage difference from top slot score value for it to be considered for pool of random slots to choose from.
# value from 0 to 1.0 where 0.0 means keep only the top scoring slots, 0.20 means choose from top 20% of values, and 1.0 means chose randomly from all slots
kSlotScoreTopPerc = 0.20
