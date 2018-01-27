"""

    Download the Data
    ~~~~~~~~~~~~~~~~~

"""
import os
import pandas as pd

OUTPATH = "data/dermatology.csv"

if not os.path.isfile(OUTPATH):
    URL = "http://archive.ics.uci.edu/ml/machine-learning-databases/dermatology/dermatology.data"
    df = pd.read_csv(URL, header=None)
    df.to_csv(OUTPATH)
