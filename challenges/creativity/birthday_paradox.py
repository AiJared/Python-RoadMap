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

def generate_birthdays(n):
    # Generate n random birthdays, with each birthday being a number between 1 and 365
    return [random.randint(1, 365) for _ in range(n)]

def birthday_paradox_simulation():
    experiments = 1000 # Number of experiments to run for each n
    for n in range(5, 101, 5):
        duplicate_count = 0
        for _ in range(experiments):
            birthdays = generate_birthdays(n)
            if has_duplicates(birthdays):
                duplicate_count += 1
    
    probability = duplicate_count / experiments
    print(f"For n = {n}, probability that two people have same birthday: {probability:.2f}")

birthday_paradox_simulation()