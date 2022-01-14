# Here we define a strucutur called a class which then carries objects
class User():
    def log(self):
        print(self)

class Teacher(User):
    def log(self):
        print("I'am a teacher")

class Customer(User):
    def __init__(self, name, membership_type): # This function will be invoked whenever we create a customer. It is called a constructor or an intializer
        self.name = name
        self.membership_type = membership_type
    
    @property
    def name(self):
        print('Getting name')
        return self._name # The _ means that the function is private
    
    @name.setter
    def name(self, name):
        print('setting name')
        return self._name = name

    @name.deleter
    def name(self, name):
        return self._name

    def update_membership(self, new_membership):
        self.membership_type = new_membership

    def __str__(self):
        print('converting to string')
        return self.name +" "+ self.membership_type
    
    def print_all_customers(customers):
        for customer in customers:
            print(customer)
    
    def __eq__(self, other):
        if self.name == other.name and self.membership_type == other.membership_type:
            return True
        return False
    __hash__ = None

    __repr__ = __str__

customers = [Customer('Caleb', 'Gold'),
            Customer('Brad', 'Bronze'),
            Teacher()]
print(customers)
customers[0].log()

# Encapsulation enables us to hide the inner details of a code and only expose those that the user of a class needs
# Inheritance allows us to have certain objects defined in a base class
# Polymorphisms allows us to address classes that share objects from the base class as the same thing.