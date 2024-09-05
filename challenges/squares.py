"""
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.
"""

def squares(n):
    total = 0                   # initialize a variable to store the sum of squares

    for num in range(1, n):     # Iterate over all numbers less than n
        total += num ** 2       # Add the square of num to total
    return total                # return the accumulated total

print(squares(5))