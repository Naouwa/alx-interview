#!/usr/bin/python3
"""
Pascal's Triangle
"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal’s triangle of n rows.
    """
    if n <= 0:
        # Return an empty list if n is less than or equal to 0
        return []

    # Initialize Pascal's triangle with the first row
    triangle = [[1]]

    # Previous row starts as the first row
    prev_row = [1]

    # Generate each row
    for i in range(1, n):
        row = [1]  # Start each row with 1
        # Calculate the middle values
        for j in range(1, i):
            # Each element is the sum of the two elements directly above it
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)  # End each row with 1
        # Update previous row to the current row
        prev_row = row
        # Append the current row to the triangle
        triangle.append(row)

    return triangle

if __name__ == "__main__":
    def print_triangle(triangle):
        """
        Helper function to print Pascal's Triangle
        """
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))
