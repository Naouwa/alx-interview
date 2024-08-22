#!/usr/bin/python3
"""
A method that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
"""


def minOperations(n: int) -> int:
    """Calculates the minimum operations needed to get n H characters"""
    copy = "H"
    paste = "H"
    operations = 0
    while len(paste) < n:
        if n % len(paste) == 0:
            operations += 2
            copy = paste
            paste += paste
        else:
            operations += 1
            paste += copy
    if len(paste) != n:
        return 0
    return operations
