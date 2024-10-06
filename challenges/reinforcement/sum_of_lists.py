# Task
"""
Write a function that takes a list of integers then returns the sum of its elements
"""

def sum_of_list(lst):
    total = 0            # Initialize a variable to hold the sum

    for num in lst:      # Loop through each element in the list
        total += num     # Add each element to the total sum
    return total         # Return the sum of all the elements

print(sum_of_list([1,2,3,4]))