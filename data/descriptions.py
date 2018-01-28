"""

    Data Descriptions
    ~~~~~~~~~~~~~~~~~

"""
# See: http://archive.ics.uci.edu/ml/datasets/Dermatology


# Clinical Attributes: (take values 0, 1, 2, 3, except age) ---
clinical = {
    1: "erythema",
    2: "scaling",
    3: "definite_borders",
    4: "itching",
    5: "koebner_phenomenon",
    6: "polygonal_papules",
    7: "follicular_papules",
    8: "oral_mucosal_involvement",
    9: "knee_and_elbow_involvement",
    10: "scalp_involvement",
    11: "family_history",
    34: "age"
}

# Histopathological Attributes: (take values 0, 1, 2, 3) ---
hist = {
    12: "melanin_incontinence",
    13: "eosinophils_in_the_infiltrate",
    14: "pnl_infiltrate",
    15: "fibrosis_of_the_papillary_dermis",
    16: "exocytosis",
    17: "acanthosis",
    18: "hyperkeratosis",
    19: "parakeratosis",
    20: "clubbing_of_the_rete_ridges",
    21: "elongation_of_the_rete_ridges",
    22: "thinning_of_the_suprapapillary_epidermis",
    23: "spongiform_pustule",
    24: "munro_microabcess",
    25: "focal_hypergranulosis",
    26: "disappearance_of_the_granular_layer",
    27: "vacuolisation_and_damage_of_basal_layer",
    28: "spongiosis",
    29: "saw-tooth_appearance_of_retes",
    30: "follicular_horn_plug",
    31: "perifollicular_parakeratosis",
    32: "inflammatory_monoluclear_inflitrate",
    33: "band_like_infiltrate"
}

all_cols = {**clinical, **hist}
all_cols[35] = "disease"

# Class Labels ---
class_labels = {
    1: "Psoriasis",
    2: "Seboreic Dermatitis",
    3: "Lichen Planus",
    4: "Pityriasis Rosea",
    5: "Cronic Dermatitis",
    6: "Pityriasis Rubra Pilaris"
}
