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