# Python Dictionaries
"""
Dictionaries are also python collection types just like lists and tuples
They store multiple data under one variable in the form of key:value.
They orderd, changeable and do not allow duplicates
Orderd means that they contain a particular form of arrangement. And this is most popular in python versions 3.7 to date.
But python versions 3.6 and earlier are unorderd meaning that they cannot be accessed using index numbers.
"""

student = {
    "name": "Kim",
    "RegNo": "TU01IC211",
    "age": 20,
    "period": 4,
    "period": 5
}
print(student)
print(type(student))

# Get the specific values from a dictionary by specifying the key
print(student["RegNo"])

# Get a specific value of from a dictionary using the get() method
x = student.get("RegNo")
print(x)

# Get all the values in form of a list using the values() method
a = student.values()
print(a)

# Get all the keys from a dictionary using the keys() method
b = student.keys()
print(b)

# Get all the items of a dictionary by using the items() method
c = student.items()
print(c)

# Adding an item in a dictionary using the update() method
student.update({"Weight": 69})
print(student)
student.update({"Height": 170})
print(student)

# Change a specific value in the dictionary by specifying it's key
student["age"] = 21
print(student)

# Removing a specific item in a dictionary using the pop() method by specifying it's key
student.pop("Height")
print(student)
# Removing the last item in a dictionary using the popitem() method
student.popitem()
print(student)
# Remove a specific item in a dictionary using del keyword by specifying it's key
del student["period"]
print(student)

# Remove the entire dictionary by using del keyword
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
print(type(thisdict))

# Remove everything from a dictionary by using clear()
thisdict.clear()
print(thisdict)

# Nested dictionaries
"""
A dictionary can contain other dictionaries. 
You can create a dictionary and create other small dictionaries inside that dict.
"""
vehicles = {
    "vehicle1": {
        "brand": "Tesla car",
        "model": "Model X",
        "year": 2021
    },
    "vehicle2": {
        "brand": "Toyota",
        "model": "Fielder",
        "year": 2015
    },
    "vehicle3": {
        "brand": "Subaru",
        "model": "X6",
        "year": 2019
    }
}

print(vehicles)
print(type(vehicles))
print(vehicles["vehicle1"])
a = vehicles.keys()
print(a)

# Create dictionaries and put them inside one large dictionary that can contain all of them
child1 = {
    "name": "Kim",
    "year": 2000
}

child2 = {
    "name": "Kate",
    "year": 2003
}

child3 = {
    "name": "Tim",
    "year": 2007
}

mother = {
    "name": "Tracy",
    "year": 1978
}

father = {
    "name": "Chandler",
    "year": 1972
}

Family = {
    "child1": child1,
    "child2": child2,
    "child3": child3,
    "Mother": mother,
    "Father": father
}
print(Family)
print(type(Family))