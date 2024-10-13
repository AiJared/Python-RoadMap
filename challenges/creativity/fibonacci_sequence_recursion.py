# Fibonacci Sequence Using Recursion
"""
A fibonacci sequence is a sequence of numbers where by each number (starting from the third) is
the sum of previous two numbers.

It goes like: 0,1,1,2,3,5,8,13,...

Mathematically: F(n) = F(n - 1) + F(n - 2)

Where: F(0) = 0 and F(1) = 1
"""

def fibonacci(n):
    # Base case
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Create recursive case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))