# Task
"""
Write a Python function that takes two sorted lists (in ascending order) and merges them into a
single sorted list(also in ascending order)

For example:
input: [1,3,5] and [2,4,6]
output: [1,2,3,4,5,6]
"""
def merge_sorted_lists(lst1, lst2):
    merged_list = []
    i,j = 0,0

    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            merged_list.append(lst1[i])
            i += 1
        else:
            merged_list.append(lst2[j])
            j += 1
    
    merged_list.extend(lst1[i:])
    merged_list.extend(lst2[j:])

    return merged_list

print(merge_sorted_lists([1,3,5], [2,4,6]))