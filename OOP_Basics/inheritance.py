# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Child class inheriting from the parent class Animal    
class Dog(Animal):

    def speak(self): # Overriding the parent class's method
        return f"{self.name} barks"

