# Task
"""
Write a python function that finds the minimum value in a list.
"""
def find_min(lst):
    min_value = lst[0]              # Assume the first element of the list is the smallest initially

    for num in lst:                 # Loop through the elements of the list
        if num < min_value:         # If you find a value smaller than min value
            min_value = num         # Update min value
    
    return min_value                # Return the minimum value       

print(find_min([2,1,3,4,5]))