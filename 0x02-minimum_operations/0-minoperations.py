#!/usr/bin/python3
"""
A method that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
"""


def minOperations(n: int) -> int:
    """Calculate the minimum operations needed to get n H characters"""
    paste_str = "H"
    operations = 0
    while len(paste_str) < n:
        if n % len(paste_str) == 0:
            operations += 2
            paste_str += paste_str
        else:
            operations += 1
            paste_str += paste_str[:len(paste_str) // 2]
    if len(paste_str) != n:
        return 0
    return operations
