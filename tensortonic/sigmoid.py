import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    z = np.array(x, dtype=float)
    out = np.empty_like(z, dtype=float)

    mask = z >= 0
    # For non-negative z
    out[mask] = 1.0 / (1.0 + np.exp(-z[mask]))
    # For negative z
    ez = np.exp(z[~mask])
    out[~mask] = ez / (1.0 + ez)

    return out