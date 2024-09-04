"""
Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators
"""

# With modulo

def even(k):
    if k%2 == 0:        # check if the modulo of k is 2
        return True
    else:
        return False
    
print(even(7))

# with division

def even(k):
    i = k / 2               # create a variable and assign it the result of k/2
    if k / 2 == int(i):     # check if the result of k/2 is an integer
        return True
    else:
        return False

print(even(7))

# Solution with Bitwise AND Operation
