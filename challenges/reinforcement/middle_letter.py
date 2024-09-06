# Middle letter

"""
Write a function named mid that takes a string as its parameter. 
Your function should extract and return the middle letter. 
If there is no middle letter, your function should return the empty string.

For example, mid("abc") should return "b" and mid("aaaa") should return "".
"""

def mid(value):
    if len(value) %2 == 0: # Check if the length of the string is even
        return " "         # Return an empty string for even length
    else:
        middle_index = len(value) // 2 # Find the middle index
        return value[middle_index]     # Return the middle index
print(mid("abc"))
print(mid("aaaa"))