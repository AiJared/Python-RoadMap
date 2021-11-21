# Inheritance in python means taking out from existing class all the methods and
# everything in there and puting them to a new class
# Let's do an example by importing a class from another python file called new.
# First ensure that both this file and the new file are in the same directory
from new import Student

class Person(Student):
    pass

p1 = Person()
print(p1.name)