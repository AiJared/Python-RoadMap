# Capital indexes
"""
Write a function named capital_indexes. 
The function takes a single parameter, which is a string. 
Your function should return a list of all the indexes in the string that have capital letters.

For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].
"""

def capital_indexes(value):
    indexes = []

    for i, char in enumerate(value): # loop through the string with both index and character
        if char.isupper():           # check if the char is upper case
            indexes.append(i)        # Add the index to the indexes list if its character is upper
    return indexes                   # return the list of indexes

value1 = capital_indexes("HeLlO")
print(value1)