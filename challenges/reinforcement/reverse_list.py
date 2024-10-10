# Task
"""
Write a Python function that takes a list as inputs then returns its elements reversed as output:
For example: Input [1,2,3,4,5], Output [5,4,3,2,1]
"""
# Using For Loop

def reverse_list(n):
    result_list = []

    for i in range(len(n)-1,-1,-1):
        result_list.append(n[i])
    
    return result_list

print(reverse_list([1,2,3,4,5]))