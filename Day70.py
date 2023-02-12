# Class Methods as Alternative Constructors 

# A constructor is a special type of method that is automatically executed when an obj. is created from a class
# there are times we want to create an obj. in diff. way, or with diff. initial values, than what is provided by the default constructor.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def from_string(cls, string):
        name, age = string.split(',')
        return cls(name, int(age))
    
# creating an object, and passing all the values as a string to it.

person = Person.from_string('Avadhoot Bhogil, 21')
print(person.name, person.age)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    @classmethod
    def from_string(cls, string):
        name, salary = string.split(',')
        return cls(name, int(salary))


# creating an object normally, using default constructor 
e1 = Employee("hello", 1200)
print(e1.name, e1.salary)

# Creating an object and passing the string to classmethods, then to constructor
# parsing the string before

string = 'Test Name, 1500'
e2 = Employee.from_string(string)
print(e2.name, e2.salary)