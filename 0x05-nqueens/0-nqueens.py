#!/usr/bin/python3
""" N queens solution finder module. """

import sys

# Validate input arguments
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

# Check if N is a valid number
if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

# Convert N to an integer and check if it's at least 4
n = int(sys.argv[1])
if n < 4:
    print("N must be at least 4")
    exit(1)


def queens(n, i=0, a=[], b=[], c=[]):
    """ Recursively find all possible positions for queens on the board.

    Args:
        n (int): Size of the board (n x n).
        i (int): Current row index.
        a (list): List of column positions of queens.
        b (list): List of diagonals (i + j) to track queen attacks.
        c (list): List of diagonals (i - j) to track queen attacks.

    Yields:
        list: A list of queen positions.
    """
    if i < n:
        for j in range(n):
            # Check if the current column and diagonals are safe
            if j not in a and i + j not in b and i - j not in c:
                # Recursively try to place the next queen
                yield from queens(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        # Yield the positions of queens when all rows are filled
        yield a


def solve(n):
    """ Solve the N queens problem and print each solution.

    Args:
        n (int): Size of the board (n x n).
    """
    # Iterate over each solution from the queens generator
    for solution in queens(n, 0):
        # Convert solution to the required format
        print([[i, s] for i, s in enumerate(solution)])


# Run the solver with the given N value
solve(n)
