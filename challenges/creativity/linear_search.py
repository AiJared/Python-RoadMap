# Task
"""
Write a Python function that takes a list and a target value as inputs then returns the index
of the target value as output. If the target value does not exist, the function should just
output None
"""

def linear_search(lst, target):
    
    # Iterate over the index values of all the elements in the list
    for i in range(0, len(lst)):
        # Return an index value that is of a provided target
        if lst[i] == target:
            return i
    
    # Return None for the target value that does not exist
    return None

print(linear_search([10, 20, 30, 40, 50], 30)) 
print(linear_search([10, 20, 30, 40, 50], 60)) 