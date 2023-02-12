# Classes and Objects 

# User defined class 
class Person:
    name = "Test Name"
    age = 20
    role = "Test Role"
    def info(self): #self parameter is a reference to the current instance of the class, & is used to access the variable that belongs to the class. Must be defined as an extra parameter
        print(f"{self.name} is of age {self.age}, and has the designation: {self.role}")

# Creating an object for the class
person1 = Person()
# print(person1.name, person1.age, person1.role)
person1.info()

person2 = Person()
person2.name = "Avadhoot"
person2.age = 21
person2.role = "Associate Analyst"
person2.info()

person3 = Person()
person3.name = "New Name"
person3.age = 23
person3.role = "New Role"
person3.info()