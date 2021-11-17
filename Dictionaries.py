# Dictionaries are used to store values in the key value pair
# They are also data types but store a value in a pair of key and value
# They are changeable which means youn can modify them
# Dictionaries does not allow two keys with the same name
my_dict = {
    'name': 'Tim', # where name is rhe key and Tim is the value
    'nationality': 'African',
    'age': 87,
    'is_tall': True,
    'Qualification': 'College',
    'friends': ['Peter', 'Paul', 'Precious']
}
print(my_dict)

# Get the value of the key name
print(my_dict['name'])

# Get the length of the dictionaries gives you the number of keys.
print(len(my_dict))

# Dictionaries also supprt multiple data types
print(my_dict['age']) # int
print(my_dict['is_tall']) # bool
print(my_dict['friends'])

# Check if it is a dictionary
print(type(my_dict))

# Use one of the keys of a dict as a value of a variable
x = my_dict['name']
print(x)