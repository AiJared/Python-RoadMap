# Task
"""
Write a python function that finds the minimum value in a list.
"""
def find_min(lst):
    min_value = lst[0]

    for num in lst:
        if num < min_value:
            min_value = num
    
    return min_value

print(find_min([2,1,3,4,5]))