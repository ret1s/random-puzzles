def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    np_true, np_pred = np.array(y_true), np.array(y_pred)
    # TP calculation
    TP = np.sum(np_true == np_pred)
    # FP & FN calculation
    FP = FN = len(y_true) - TP
    # Micro-F1 calculation
    micro_f1 = 2*TP / (2*TP + FP + FN)
    return micro_f1