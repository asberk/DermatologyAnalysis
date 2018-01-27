"""

    Support Tools
    ~~~~~~~~~~~~~

"""
import pandas as pd
from itertools import zip_longest

def list_to_df(l, n=4, fillvalue=''):
    """Conver a list into a dataframe, breaking every `n` items."""
    # https://stackoverflow.com/a/312644/4898004
    summary_df = pd.DataFrame(list(zip_longest(*[iter(l)] * n, fillvalue=fillvalue)))
    summary_df.index = [""] * summary_df.shape[0]
    summary_df.columns = [""] * summary_df.shape[1]
    return summary_df
