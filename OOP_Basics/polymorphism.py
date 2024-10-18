# Create class Animal
class Animal:
    # constructor method to initialize the attribute name
    def __init__(self, name):
        self.name = name

    # method speak to describe a sound that an animal makes
    def speak(self):
        return f"{self.name} makes a sound."

# Create a class Dog to inherit from the class Animal. In this case Animal acts as superclass
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"

