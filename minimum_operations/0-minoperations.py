#!/usr/bin/python3
"""Module that defines a function to compute minimum copy/paste ops."""


def minOperations(n):
    """Compute the fewest Copy All / Paste operations to reach n H's.

    Args:
        n: the target number of H characters.

    Returns:
        The minimum number of operations, or 0 if n is impossible
        to achieve (n < 2).
    """
    if n < 2:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
