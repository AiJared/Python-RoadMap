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