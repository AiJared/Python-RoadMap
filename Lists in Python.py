countries = ['United Kingdom', 'Ghana', 'Nigeria', 'Australia', 'New Zealand']
print(countries)

# Print the index numbers of various values of a list
print(countries[0])
print(countries[2][0])

# Print from index 1 to the end
print(countries[1:])

# Print a range of values in the list
print(countries[1:4])

# Print type of the list
print(type(countries))

# Change the value of a particular index
countries[0] = 'United States'
print(countries)
countries[3] = 'Canada'
print(countries)

# Getting a list from the last value of the list using '-'
print(countries[-1])

# Getting the number of values of the list using len() function
print(len(countries))

# Multiple data types in a list
countries = ['United Kingdom', 2, True, 'Australia']
print(countries)
print(countries[2])
print(type(countries))
print(type(countries[2]))

# Using a list constractor
countries = list(('Nigeria', 34, False))
print(countries)