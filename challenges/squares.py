"""
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.
"""

def squares(n):
    total = 0

    for num in range(1, n):
        total += num ** 2
    return total

print(squares(5))