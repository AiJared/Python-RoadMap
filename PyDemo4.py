#Lists in python they multiple data in one memory location
from pyparsing import countedArray


countries = ["Kenya", "Uganda", "Tanzania", "Ethiopia"]
print(countries)
print(type(countries))
print(countries[1:4])
countries2 = ["Cameroon", "Nigeria", "Ghana", "Senegal", "Nigeria"]
# Extend method puts a list inside another list
countries.extend(countries2)
print(countries)
# Append method adds an item to the end of the list
countries.append("Somalia")
print(countries)
# Insert method adds an item to our list at a specif position
countries2.insert(1, "Mali")
print(countries2)
# count methods tells us how many times an item appears in a list
print(countries2.count("Nigeria"))
# reverse methode rearranges data in a list from the last one to the first one
countries2.reverse()
print(countries2)
# sort method arranges the data in the list alphabetically
countries.sort()
print(countries)
# pop method removes the data that it is at end of the list
countries2.pop()
print(countries2)
# remove method removes a specific data in a list
countries.remove("Somalia")
print(countries)