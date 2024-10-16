# Encapsulation with Public and Private Attributes
class Person:

    def __init__(self, name, age):
        self.name = name # Public attribute
        self.__age = age # Private attribute

    def describe(self):
        return f"{self.name} is {self.__age} years old."
    
    def get_age(self):
        return self.__age


