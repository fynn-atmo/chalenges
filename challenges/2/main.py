def ohmsLaw(v, r, i):
    """Write your code here to calculate the missing value.

    Args:
        v (int or None): Voltage or None
        r (int or None): Resistance  or None
        i (int or None): Current  or None

    Returns: The missing value calculated to 2dp or "invalid".
    """
    if (not v) and i and r:
        return round((r*i), 2)
    elif (not r) and v and i:
        return round((v/i), 2)
    elif (not i) and v and r:
        return round((v/r), 2)
    else:
        return "Invalid"