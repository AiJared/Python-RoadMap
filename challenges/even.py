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
"""
In Python you can determine if a number is even or odd using the bitwise AND operator &.
Specifically, even numbers has their least significant bit (rightmost bit) set to 0.
The number 1 in binary is represented as 0001. Therefore you can use k & 1 to check the
least significant bit of k.

If k & 1 is 0 - k is even
If k & 1 is 1 - k is odd
"""

def is_even(k):
    return k & 1 == 0 # bitwise AND operation to check if the least significant bit of k is 0

print(is_even(7))
print(is_even(8))