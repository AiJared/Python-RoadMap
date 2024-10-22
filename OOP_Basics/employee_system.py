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

