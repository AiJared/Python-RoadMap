# Class attributes are attributes that are specific to a class and not an instance
class Person:
    number_of_people = 0

    def _init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people_()

    @classmethod
    def add_person(cls):
        cls.number_of_people() += 1

p1 = Person("Tim")
p2 = Person("Jill")
print(Person.number_of_people_())