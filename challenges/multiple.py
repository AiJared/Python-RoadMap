"""
Write a short Python function, is multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise.
"""
def is_multiple(n, m):
    i = 2
    if n / m == i:
        return True
    else: 
        return False

print(is_multiple(9, 3))
