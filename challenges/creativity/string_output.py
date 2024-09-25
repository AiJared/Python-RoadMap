"""
Write a Python program that outputs all possible strings formed by using
the characters c , a , t , d , o , and g exactly once.
"""
from itertools import permutations

def string_output():
    characters = ["c", "a", "t", "d", "o", "g"]

    # Generate all the permutations of the characters
    for perm in permutations(characters):
        # join the tuple of characters into a single string
        print(''.join(perm))

string_output() 