# What is Memoization
"""
Memoization is an optimization technique used to store the results of expensive function calls
and then reuse them whenever the same inputs occur again. Instead of recalculating the Fibonacci
of of a particular n multiple times, we store it once then reuse it.
"""

# Python Memoization using a Dictionary
"""
We can use a dictionary to store the results of a fibonacci calculation then check if the result
of n is already computed before making a recursive call.
"""
