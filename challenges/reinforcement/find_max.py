# Task
"""
Write a function to find the maximum value in a list. However, do not use the built-in max() function
apply the logic on your own.
"""
def find_max(lst):
    max_value = lst[0]          # Assume the first element is the largest initially

    for num in lst:             # Loop through each element of the list
        if num > max_value:     # If you find a value larger than max value
            max_value = num     # Update max value
    return max_value            # Return the largest value

print(find_max([1,2,3,4]))