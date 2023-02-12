# Inheritance 
# When a class is derived from another class, the child class inherits all the public & protected properties and methods from the parent class.

# Defining the Parent Class 
class Employee:
    def __init__(self, name, id):
        self.name =  name
        self.id = id
    
    def showDetails(self):
        print(f"The Name of the Employee: {self.id} is {self.name}")
    
a = Employee('Avadhoot Bhogil', 2312)
a.showDetails()
b = Employee('Test Name', 1231)
b.showDetails()

# Defining the Child class, which is inherited from the parent class Employee
class Manager(Employee):
    def manage(self):
        print("Hello, I am the Manager")

c = Manager('Managing', 233)
c.manage()
# Accessing the methods of parent class 
c.showDetails()
