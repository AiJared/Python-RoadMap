# Type check

"""
Write a function named only_ints that takes two parameters. Your function should return True if both parameters are integers, and False otherwise.

For example, calling only_ints(1, 2) should return True, while calling only_ints("a", 1) should return False.
"""

def only_ints(inta, intb):
    if isinstance(inta, int) and isinstance(intb, int):
        return True
    else:
        return False
    
print(only_ints(1, 2))