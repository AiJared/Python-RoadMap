# Task
"""
Write a Python function that takes a list and a target value as inputs then returns the index
of the target value as output. If the target value does not exist, the function should just
output -1
"""

def linear_search(lst, target):
    
    for i in range(0, len(lst)):
        if lst[i] == target:
            return i
    
    return -1

print(linear_search([10, 20, 30, 40, 50], 30)) 
print(linear_search([10, 20, 30, 40, 50], 60)) 