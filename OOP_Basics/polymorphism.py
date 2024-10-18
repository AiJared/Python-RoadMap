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

# Create a class Cat to inherit from the class Animal. In this case Animal acts as superclass
class Cat(Animal):
    def speak(self):
        return f"{self.name} meows."

# create a list of animals
animals = [Dog("Buddy"), Cat("Whiskers")]

# Loop through the list of animals and output their sounds
for animal in animals:
    print(animal.speak())