# What is a set
"""
A set is an unorderd sequence/collection of unique/distinct items.
This means that:

1. Set does not have duplicates
2. It is unordered meaning that you cannot access items using index numbers as you would in list

"""

# Key Properties of a Set:
"""
1. Unique - All the elements of a set are not the same. If you try to an existing element it
won't be added.
2. Unordered - All the elements in a set are not in any order. Meaning that you cannot rely
on order when iterating through a set or printing its elements.
3. Mutable - You can add or remove elements from a set.
"""

# Basic Set Operations:
# 1. Creating a set

"""
You can create a set by just creating a variable and a collection of its elemets in curly braces
"""
numbers = {1,2,3,4,5}
print(numbers)

"""
You can also use built-in set methos. Perfect for creating an empty set.
"""
empty_set = set()
print(empty_set)

# 2. Adding elements to a set
numbers.add(5)
print(numbers)

## Try to add an existing element
numbers.add(4)
print(numbers) # the new element 4 is ignored because it already exists

# 3. Removing elements from a set
numbers.remove(5)
print(numbers)

## Using discard won't throw an error if the element does not exist
numbers.discard(10)
print(numbers)

# Set Operations
"""
Set are useful for carrying out mathematical operations such as union, intersection and different.
1. Union (|) - Combines elements from both sets without intersection(without duplicates).
2. Intersection (&) - Returns elements that are only common to both sets.
3. Difference (-) - Returns only elements that are in one set and not the other.
"""

# 1. Union
nums1 = {1,2,3,4}
nums2 = {3,4,5,6}

print(nums1 | nums2) # combine all unique elements

# 2. Intersection
print(nums1 & nums2) # return elements in both sets

# 3. Difference
print(nums1 - nums2) # return elements that are only in the first set and not the second

# Checking for Membership
"""
You can check if an element is a member of a set using the in keyword.
"""
print(2 in numbers)
print(10 in numbers)

# Why Use Sets?
"""
There are a number of reasons to use sets.
1. Uniqueness: If you want to ensure that all the values in a sequence are unique, use sets.
(for example you can eliminate duplicate values in a list using a set).
2. Faster operations: To check if a value is a member of a set you just need to use the keyword in
which is faster than doing the same for a list.
"""

# Example: Removing Duplicates From a List
"""
One common use case is to remove duplicates from a list as shown below.
"""
nums = [1,2,2,3,4,4,5,6]
unique_nums = list(set(nums)) # convert to set the back to list
print(unique_nums)