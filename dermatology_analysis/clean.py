"""

    Clean the Data
    ~~~~~~~~~~~~~~

"""
import pandas as pd
from data.descriptions import all_cols, clinical, class_labels

# -----------------------------------------------------------------------------
# Load Data
# -----------------------------------------------------------------------------

df = pd.read_csv("data/dermatology.csv", na_values='?')

# -----------------------------------------------------------------------------
# Clean Data
# -----------------------------------------------------------------------------

# Update col names
df.columns = [all_cols[int(i) + 1] for i in df.columns]

# make the disease labels human readable
df["disease"] = df["disease"].replace(class_labels)

# -----------------------------------------------------------------------------
# Subset to Clinical Columns
# -----------------------------------------------------------------------------

df = df[["disease"] + list(clinical.values())]
