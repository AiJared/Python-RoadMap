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
def fibonacci_memo(n, memo={}):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # check if n is in the memo dictionary
    if n not in memo:
        # calculate the fibonacci of n if it is not in memo
        memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    
    return memo[n]

print(fibonacci_memo(5))
print(fibonacci_memo(10))
print(fibonacci_memo(50))