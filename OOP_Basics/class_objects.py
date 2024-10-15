# Define a class called car
class Car:
    # Create a constructor method to intialize the attributes (variables)
    def __init__(self, brand, model, year):
        self.brand = brand # attribute (variable) called brand
        self.model = model # attribute called model
        self.year = year # attribute called year

    # method to describe the car
    def describe(self):
        return f"This car is {self.brand}, {self.model} manufactured in {self.year}"
    
# Create an object (instance) of the class
my_car = Car("Toyota", "Corolla", 2020)

# Accessing the objects of the class
print(my_car.brand)
print(my_car.describe())
print(my_car.model)
print(my_car.year)