"""
Write a Python program that outputs all possible strings formed by using
the characters c , a , t , d , o , and g exactly once.
"""
from itertools import permutations

def string_output():
    characters = ["c", "a", "t", "d", "o", "g"]

    for perm in permutations(characters):
        print(''.join(perm))

string_output() 