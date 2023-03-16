# Hybrid & Hierarchical Inheritance 
'''
Hybrid inheritance - It is a combination of multiple inheritance, & a single inheritance in OOP
It is a type of inheritance in which multiple inheritance is used to inherit the properties of multiple base classes into a single derived class.
and the single inheritance is used to inherit the properties of the derived class into a sub-derived class

Syntax - 

class BaseClass:
    pass
class DC1(BaseClass):
    pass
class DC2(BaseClass):
    pass
class DC3(DC1, DC2)

Hierarchical inheritance - It is a type of inheritance, where multiple subclasses inherit from a single base class

Syntax -

class BaseClass:
    pass
class D1(BaseClass):
    pass
class D2(BaseClass):
    pass
class D3(D1):
    pass
class D4(D2):
    pass
'''

# Hybrid Inheritance
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_details(self):
        # print(f"The Name of the Person is {self.name}, and the age is {self.age}")
        return (f"The Name of the Person is {self.name}, and the age is {self.age}")
    
class Engineer(Person):
    def __init__(self, name, age, qualify, branch):
        Person.__init__(self, name, age)
        self.qualify = qualify
        self.branch = branch
    def show_details(self):
        # print(f"{super().show_details()}, {self.name} is an Engineer with {self.qualify} - {self.branch} Qualification ")
        return (f"{Person.show_details(self)}. {self.name} is an Engineer with {self.qualify} - {self.branch} Qualification ")
    
class Doctor(Person):
    def __init__(self, name, age, degree, grad):
        Person.__init__(self, name, age)
        self.degree = degree
        self.grad = grad
    def show_details(self):
        # print(f"{super().show_details()}, {self.name} is an Engineer with {self.qualify} - {self.branch} Qualification ")
        return (f"{Person.show_details(self)}. {self.name} is a doctor with {self.degree} - {self.grad} Qualification ")

class Student(Engineer, Doctor):
    def __init__(self, name, age, stream):
        self.stream = stream
        # Person.__init__(self, name, age)
        Engineer.__init__(self, name, age, qualify='Engineer', branch='BE')
        Doctor.__init__(self, name, age, degree='BDS', grad='doctor')

    def choose_stream(self):
        choose = int(input("Enter a stream you want to percieve. 1 - Engineer, 2 - Doctor: "))
        if (choose == 1):
            return f"{self.stream} Stream. {Engineer.show_details(self)}"
        elif (choose == 2):
            return f"{self.stream} Stream. {Doctor.show_details(self)}"
        else:
            return "Please choose from above options"
        
# creating an obj of Engineer class 

# e = Engineer('Avadhoot', 21, 'B.E', 'IT')
# print(e.show_details())

# d = Doctor('TestDoctor', 26, 'Dentist', 'BDS')
# print(d.show_details())

# child class dervied using hybrid inheritance
s1 = Student('Avadhoot', 18, 'Science')
print(s1.choose_stream())

# Hierarchical inheritance

class CEO:
    def __init__(self, name, age, role):
        self.name =  name
        self.age = age
        self.role = role
    
    def details(self):
        return f"{self.name} is of age {self.age} has a designation: {self.role}"

class VP(CEO):
    def __init__(self, name, age, role, reports_to = 'CEO'):
        CEO.__init__(self, name, age, role = 'VP')
        self.reports_to = reports_to
        self.role = role

    def details(self):
        return (f"{CEO.details(self)}, {self.name} reports to {self.reports_to}")

class assistantVP(CEO):
    def __init__(self, name, age, role = 'assistantVP', reports_to = 'VP'):
        CEO.__init__(self, name, age, role)
        self.reports_to = reports_to
        self.role = role

    def details(self):
        return (f"{CEO.details(self)}, {self.name} reports to {self.reports_to}")

class Manager(assistantVP):
    def __init__(self, name, age, reports_to = 'assistantVP'):
        assistantVP.__init__(self, name, age, role = 'Manager')
        self.reports_to = reports_to

    def details(self):
        return (f"{assistantVP.details(self)}, and Manages the Team")

# creating an obj for assitantVP and manager class 

ap = assistantVP('Jitesh', 32)
print(ap.details())

mn = Manager('Ram', 40)
print(mn.details())
