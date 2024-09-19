"""
Give an example of a Python code fragment that attempts to write an element to 
a list based on an index that may be out of bounds. If that index
is out of bounds, the program should catch the exception that results, and
print the following error message:
“Don’t try buffer overflow attacks in Python!
"""

a = [1,2,3,4,5]

try:
    # Try to access index 5 which is out of bounds
    a[5] = 6

# Throw an IndexError
except IndexError:
    print("Don't try buffer overflow attacks in Python!")