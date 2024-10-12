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

