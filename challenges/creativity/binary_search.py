# Task
"""
Binary search enables searching for an element in a sorted list faster because it cuts
the list in half and compares the target with the mid element if the mid element is the
target value it returns if not it adjusts its search on the basis of whether the target
is less than or greater than the mid element. If the target is less than the mid element, 
it discards the elements that are greater than the mid and the mid included then creates another
mid for the remaining elements, if it is greater than the initial mid it does the opposite.
The process is repeated unti the target value is either found or not.
"""
# Steps
"""
1. Find the middle element of the list.
2. If the target equals the middle element return the index of the middle element.
3. If the target is less than the middle element repeat search for the left half.
4. If the target is greater than the middle element, repeat search for the right half.
4. If the range becomes empty return(-1), target not found.
"""

def binary_search(lst, target):
    # Create left and right variables for storing each half of the list
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2 # Find the middle element

        # return the index of the middle element if it equals the target
        if lst[mid] == target:
            return mid

        # Adjust search to the left side if the target is less than the middle element
        elif lst[mid] > target:
            right = mid - 1
        # Adjust search to the right side if the target is greater than the middle element
        else:
            left = mid + 1
    
    # return None if the range becomes empty or target is not found
    return None

print(binary_search([10, 20, 30, 40, 50], 30))
print(binary_search([10, 20, 30, 40, 50], 60))