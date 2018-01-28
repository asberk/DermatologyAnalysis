"""

    Support Tools
    ~~~~~~~~~~~~~

"""
import pandas as pd
from itertools import zip_longest
from scipy.spatial.distance import pdist, squareform


def list_to_df(l, n=4, fillvalue=''):
    """Conver a list, `l` into a dataframe, breaking every `n` items."""
    # https://stackoverflow.com/a/312644/4898004
    summary_df = pd.DataFrame(list(zip_longest(*[iter(l)] * n, fillvalue=fillvalue)))
    summary_df.index = [""] * summary_df.shape[0]
    summary_df.columns = [""] * summary_df.shape[1]
    return summary_df


def dist(matix):
    """Roughly equal to R's dist()` function for
    computing the distance between rows."""
    # https://stackoverflow.com/a/38205609/4898004
    distances = pdist(matix, metric='euclidean')
    dist_matrix = squareform(distances)
    return dist_matrix
