from abc import ABC, abstractmethod

# Define an abstract class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass # Abstract method, no implementation

    @abstractmethod
    def perimeter(self):
        pass # Abstract method, no implementation

# Concrete classes must implement abstract methods
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Instantiate the concrete classes

rec = Rectangle(4, 5)
circle = Circle(3) 

print(f"Rectangle Area: {rec.area()}, Rectangle Perimeter: {rec.perimeter()}")
print(f"Circle Area: {circle.area()}, Circle Perimenter: {circle.perimeter()}")
