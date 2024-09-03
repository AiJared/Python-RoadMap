"""
Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators
"""

# With modulo
def even(k):
    if k%2 == 0:
        return True
    else:
        return False
    
print(even(7))