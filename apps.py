# Python Dictionaries
"""
Collection types that store data in terms of key and value.
Dictionaries are orderd, changeable and does not allow duplicates.
Python 3.7 and later versions are orderd while 3.6 and earlier vasions are unorderd.
"""
car = {
    "brand": "Ford",
    "model": "Model X",
    "year": 2012,
}
print(car)
print(type(car))
# We can output a value by specifying it's key
print(car["brand"])

# we can output a list of keys using the keys() method
x = car.keys()
print(x)
# We can change the values of keys by specifying the keys and the values
car["year"] = 2020
print(car["year"])
# we can also use the update() to make changes to a dictionary
car.update({"year": 2018})
print(car)
# We can use the values() method to output a list of all values in a dictionary
a = car.values()
print(a)
# we use items() methods to get a list of all the items in a dictionary
c = car.items()
print(c)
# we can use get() method to get the values a specific keys
b = car.get("model")
print(b)
# Add an item using the update method
car.update({"color": "red"})
print(car)
# Using the pop() with a specifeid key to remove an item
car.pop("color")
print(car)
# Using popitem() to remove the last item inserted in our dictionary
car.popitem()
print(car)

student  = {
    "name": "Jared",
    "RegNo": "Ic211",
    "age": 20,
    "year": 2021
}
# Using del keyword to remove a specific item using a specified key
del student["year"]
print(student)
# Using clear method to make the dictionary empty
student.clear()
print(student)

# Nested Dictionaries
"""
A dictionary can contain dictionaries as show in the programs below.
"""
# We can aslo create dictionaries outside and create another big dictionary that will contain all of them
child1 = {
    "name": "Emil",
    "year": 2004
}

child2 = {
    "name": "Tobias",
    "year": 2007
}

child3 = {
    "name": "Linus",
    "year": 2011
}

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}

print(child1)
print(child2)
print(child3)
print(myfamily)