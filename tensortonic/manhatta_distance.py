import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    np_x, np_y = np.array(x), np.array(y)
    manhatta = float(np.abs(np_x - np_y).sum())
    return manhatta