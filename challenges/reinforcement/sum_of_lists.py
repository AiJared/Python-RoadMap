# Task
"""
Write a function that takes a list of integers then returns the sum of its elements
"""

def sum_of_list(lst):
    total = 0

    for num in lst:
        total += num
    return total

print(sum_of_list([1,2,3,4]))