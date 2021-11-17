# Extend method puts a list inside another list
list1 = [1, 2, 3, 4, 5]
list2 = ['banana', 'apples', 'mango', 'oranges']
list1.extend(list2)
print(list1)

# Append method adds values to a list
list2.append('cherry')
print(list2)

# Get the length of list2
print(len(list2))

# Put cherry in between banana and apples using insert method
list2.insert(1, 'cherry')
print(list2)

# Remove a value from a list using remove method
list2.remove('banana')
print(list2)

# Delete list values to clear everything using clear method
list2.clear()
print(list2)

# Print the index number of a value in a list
list2 = ['banana', 'apples', 'mango', 'oranges', 'mango']
print(list2.index('mango'))

# Print how many times a value appears in a list
print(list2.count('mango'))

# Print values of a list in ascending order
list1 = [4, 3, 5, 1, 2]#
list1.sort()
print(list1)

# Print a list from the last one to the first one
list2.reverse()
print(list2)

# Create a duplicate of a list
list3 = list2.copy()

# Remove the last value in a list using the pop method
list2.pop()
print(list2)

# Remove a specific value of a list using pop index method
list2.pop(1)
print(list2)

# Remove a specific value of a list using delete method
list2 = ['banana', 'apples', 'mango', 'oranges', 'mango']
del list2[0]
print(list2)