"""

    Clean the Data
    ~~~~~~~~~~~~~~

"""
import json
import numpy as np
import pandas as pd
from data.descriptions import all_cols, class_labels

# -----------------------------------------------------------------------------
# Load Data
# -----------------------------------------------------------------------------

df = pd.read_csv("data/dermatology.csv", na_values='?')

# -----------------------------------------------------------------------------
# Clean Data
# -----------------------------------------------------------------------------

# Update col names
df.columns = [all_cols[int(i) + 1] for i in df.columns]

# make the labels human readable
df["label"] = df["label"].replace(class_labels)
