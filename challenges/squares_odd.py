"""
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.
"""

def squares(n):
    total = 0                     # initialize a variable for storing sum of squares

    for num in range(1, n):       # iterate over all positive integers less than n
        if num % 2 != 0:          # check for positive odd numbers
            total += num ** 2     # sum up the squares of all the positive odd numbers less than n
    return total                  # return the cummulated total

print(squares(5))

# Using List Comprehension and the sum() Function
def squares(n):
    return sum(num ** 2 for num in range(1, n) if num % 2 != 0)

print(squares(5))