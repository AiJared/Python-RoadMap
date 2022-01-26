# Lists are data types that helps you to store a list of values
from copy import copy
names = ["John", "James", "Linda", "Grace", "Kim", "Brenda", "Joseph", "Caleb"]
print(names)
#Outputs the first value
print(names[0])
#Outputs the first two values of the list
print(names[0:2])
#Outputing from index number 2 to the last value in the list.
print(names[2:])
# Confirm that this is a list type
print(type(names))
# Getting the list from the last value using '-'
print(names[-1])
print(names[-2])
print(names[-3])
# A list can hold values of various/multiple data types as long as the syntax remain intact.
counntries = ["United States", 2, True, 10.55, "Kenya"]
print(counntries)
print(type(counntries))
print(counntries[0])
print(counntries[2])
# Using a list constractor
countries2 = list(("Nigeria", "Ghana", "Burundi", "Egypt", "Canada", "Australia"))
print(countries2)
print(type(countries2))
# Extending a list with another list using extend() method
counntries.extend(countries2)
print(counntries)
# Adding a value to the end of the list using append() method
counntries.append("China")
print(counntries)
print(len(counntries))
#Using insert method to add a value to a list between other values
counntries.insert(1, "Germany")
print(counntries)
counntries.insert(4, "Cameroon")
print(counntries)
# Removing a value from a list using remove() method
counntries.remove(10.55)
print(counntries)
# Using the reverse() method to change the order of values in a list
#counntries.reverse()
#print(counntries)
# Crearing a duplicate of a list
countries3 = copy(countries2)
print(countries3)
# Count the number of times a value appears in a list using count() method
countries2.append("Nigeria")
print(countries2.count("Nigeria"))
# Soughting the values inside our list using the sort() method
countries2.sort()
print(countries2)
# Removing the last value in a list using pop() method
countries2.pop()
print(countries2)
#Remove a value in a list using pop() with the values index number
counntries.pop(2)
print(counntries)
counntries.pop(2)
print(counntries)
# Remove a specific value kutumia delete() method
del counntries[1]
print(counntries)