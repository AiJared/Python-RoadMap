"""
The birthday paradox says that the probability that two people in a room
will have the same birthday is more than half, provided n, the number of
people in the room, is more than 23. This property is not really a paradox,
but many people find it surprising. Design a Python program that can test
this paradox by a series of experiments on randomly generated birthdays,
which test this paradox for n = 5,10,15,20,... ,100.
"""
import random

def has_duplicates(birthdays):
    # Return True if there are duplicate birthdays in the list
    return len(birthdays) != len(set(birthdays))

