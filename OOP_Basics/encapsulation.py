# Encapsulation with Public and Private Attributes
class Person:
    # Constructor initializes the attributes name and age
    def __init__(self, name, age):
        self.name = name # Public attribute
        self.__age = age # Private attribute

    # method that describes the object "Person"
    def describe(self):
        return f"{self.name} is {self.__age} years old."
    
    # Method to access the private attribute age
    def get_age(self):
        return self.__age

# First object
person1 = Person("Alice", 30)

# Access attributes and methodes of the object person1
print(person1.name)

# trying to access the age of the object directly as shown below will raise an Attribute error
# print(person1.__age)

# Instead access it via the public get_age() method as shown below
print(person1.get_age())