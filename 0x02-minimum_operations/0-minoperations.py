#!/usr/bin/python3
"""
A method that calc the fewest no of operations to achieve n 'H' characters.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations to achieve n 'H' characters.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum no of operations required, or 0 if n is less than 1.
    """
    if n < 2:
        return 0  # Impossible or trivial case

    operations = 0
    factor = 2

    # Factorize n
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
