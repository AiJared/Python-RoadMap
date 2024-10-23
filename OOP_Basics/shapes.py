from abc import ABC, abstractmethod

# Abstract base class
class Shape(ABC):
    # Abstract method that must be implemented by other classes.
    @abstractmethod
    def area(self):
        pass

# Concrete classes that inherits the abstract base class Shape
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    # abstract method area that must be implemented from the abstract base class Shape
    def area(self):
        return 0.5 * self.base * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    # abstract method area that must be implemented from the abstract base class Shape
    def area(self):
        return self.side * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # abstract method area that must be implemented from the abstract base class Shape
    def area(self):
        return 3.14 * self.radius ** 2

# Function that takes any shape and prints its area using Polymorphism
def print_area(shape: Shape):
    print(f"The area of shape is {shape.area()}") 

# Instantiating the objects of the concrete classes
triangle = Triangle(10, 5)
square = Square(4)
circle = Circle(3)

# Print areas of the shapes using polymorphism
print_area(triangle)
print_area(square)
print_area(circle)

# You can also create a list of objects of concrete classes
shapes = [Triangle(10, 5), Square(4), Circle(3)]

# Then loop through them as you call the area() method
for shape in shapes:
    print(shape.area())