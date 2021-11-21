# python is an object oriented programming
# Anything that deals with classes objects and functions is object oriented
# They all are python features
class Myclass: # this is the class
    x = 5 # x is the object of the class

p1 = Myclass()
print(p1.x)

# Using the init function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Allowing the user to input values
name = input('Enter your name: ')
age = input('Enter your age: ')
p1 = Person(name, age)
print(p1.name)
print(p1.age)

# Use 'del' to delete any object in a class or even a class itself
# Use 'pass' to bypass any error incase of an empty class with no objects.
class Pyclass:
    pass