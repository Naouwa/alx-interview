#!/usr/bin/python3
"""
A method that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
"""


def minOperation(n: int) -> int:
    """The minimum operations needed to get n H characters"""
    copy = "H"
    paste = "H"
    operation = 0
    while (len(paste) < n):
        if n % (len(paste)) == 0:
            operation += 2
            copy = paste
            paste += paste
        else:
            operation += 1
            paste += copy
    if (len(paste)) != n:
        return 0
    return operation
