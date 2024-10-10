# Task
"""
Write a Python function that takes a list as inputs then returns its elements reversed as output:
For example: Input [1,2,3,4,5], Output [5,4,3,2,1]
"""
# Using For Loop

def reverse_list(n):
    result_list = [] # Create an empty list to store elements of the reversed list

    for i in range(len(n)-1,-1,-1): # Loop through the original list starting from the end
        result_list.append(n[i]) # Add elements of the original list to the new list in reverse order
    
    return result_list # return the new reversed list

print(reverse_list([1,2,3,4,5]))

# Using Slicing

def reverse_lst(n):
    return n[::-1] # return the original list in reverse order

print(reverse_lst([1,2,3,4,5]))