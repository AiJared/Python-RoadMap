# What is an Array
"""
An array is the simplest and most widely used data structure. It is a selection of components
(values and variables) all of the same data type in a contingous memory location.

Key Features:
 - Fixed size:- The size of an array is specified at the time of its creation.
 - Indexing:- Elements are accessed with an index number, with indexinf starting from 0
 - Random access:- You can access elements at any position using their index numbers making
 lookup fast, at O(1), that is, contant time.

Operations of an array
 - Accessing: You can access elements by their index.
 - Insertion: You can insert elements at the end or in the middle, but inserting in between
 the array requires shifting elements, so it is less efficient.
 - Deletion: Similar to insertion, deleting from beginning or in the middle requires
 shifting elements.
"""
# Creating an array in Python
arr = [1,2,3,4,5]
# Accessing an element of an array
print(arr[2])
# Adding an element at the end of the array
arr.append(6)
# Inserting an element at a given position
arr.insert(2, 7)
print(arr)
# Removing an element at the end of the array
arr.pop()
print(arr)
# Removing a specific element
arr.pop(2)
print(arr)