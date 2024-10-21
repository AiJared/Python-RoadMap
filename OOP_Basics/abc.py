from abc import ABC, abstractmethod

# Define an abstract class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass # Abstract method, no implementation

    @abstractmethod
    def perimeter(self):
        pass # Abstract method, no implementation
