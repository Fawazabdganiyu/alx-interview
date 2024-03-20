#!/usr/bin/python3
"""Definition of `minOperations` function
"""


def minOperations(n):
    """Calculates the fewest number of operations needed to result in exactly
    n H characters in the file
    """
    if n <= 1:
        return 0

    # Get all the prime factors of the given number
    factors = []
    div = 2
    while n > 1:
        if n % div == 0:
            factors.append(div)
            n //= div
        else:
            div += 1

    return sum(factors)
