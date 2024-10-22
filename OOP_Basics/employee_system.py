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
        return f"Fulltime Employee: {self.name}, Salary: {self.calculate_salary()}"

# Concrete class PartTimeEmployee that inherits abstract class Employee
class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    
    # must implement abstract methods from abstract class Employee
    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked
    
    def display_employee_details(self):
        return f"Part Time Employee: {self.name}, Salary: ${self.calculate_salary()}"

# Instantiating the objects of the concrete classes
fulltimeemployee = FullTimeEmployee("Alice", 20000)
partitmeemployee = PartTimeEmployee("Bob", 75, 80) 

print(fulltimeemployee.display_employee_details())
print(partitmeemployee.display_employee_details())