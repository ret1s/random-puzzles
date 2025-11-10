import numpy as np

def cross_entropy_loss(y_true, y_pred):
    """
    Compute average cross-entropy loss for multi-class classification.
    """
    # Write code here
    y_true = np.asarray(y_true, dtype=np.int64)
    y_pred = np.asarray(y_pred, dtype=np.float64)

    # Basic shape checks
    if y_pred.ndim != 2:
        raise ValueError(f"y_pred must be 2D (N, C), got shape {y_pred.shape}")
    if y_true.ndim != 1:
        raise ValueError(f"y_true must be 1D (N,), got shape {y_true.shape}")
    if y_true.shape[0] != y_pred.shape[0]:
        raise ValueError(f"Mismatched first dimension: y_true N={y_true.shape[0]} vs y_pred N={y_pred.shape[0]}")

    N, C = y_pred.shape

    # Validate class indices
    if (y_true < 0).any() or (y_true >= C).any():
        raise ValueError(f"y_true contains invalid class indices for C={C}")

    # Pick the predicted probability assigned to the true class for each sample
    p_true = y_pred[np.arange(N), y_true]

    # Since probs are guaranteed > 0, np.log is safe (no need to clip)
    loss = -np.mean(np.log(p_true))
    return float(loss)