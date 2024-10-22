from abc import ABC, abstractmethod

# Abstract class Employee
class Employee(ABC):
    # abstract method calculate_salary
    @abstractmethod
    def calculate_salary(self):
        pass

    # Abstract method display_employee_details
    @abstractmethod
    def display_employee_details(self):
        pass

# Concrete class FullTimeEmployee that inherits abstract class Employee
class FullTimeEmployee(Employee):

    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
    
    # must implement abstract methods from abstract class Employee
    def calculate_salary(self):
        return self.base_salary
    
    def display_employee_details(self):
        return f"{self.name}'s salary is {self.base_salary}"
