def capToFront(input):
    """Write your function here, which will return a string with all the capital letters at the front.

    Args:
        input (str): The input string.

    Returns:
        str: The result.
    """
    lower = []
    upper = []
    for char in input:
        if char.isupper():
            upper.append(char)
        else:
            lower.append(char)
    return "".join(lower)
