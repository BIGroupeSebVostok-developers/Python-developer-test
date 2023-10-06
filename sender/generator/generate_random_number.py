import random


def generate_random_number(
    *,
    length: int,
) -> str:
    """
    Generate a random alpha string of length

    Parameters
    ----------
    length : int
        The lenght of generating string.

    Returns
    -------
    str
        Generated string.

    Examples
    --------
    >>> generate_random_number(length=2)
    "92"  
    """
    return "".join(random.choice(list(map(str, range(10)))) for _ in range(length))