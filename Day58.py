# Constructors 

# A constructor is a special method in a class used to create and intialize an obj. of a class. It gets invoked automatically when an obj. of a class is created.
# It cannot return any value other than None 


# 1. Default Constructor - doesn't accept any arguments from the obj. & has only 1 argument, self.
class newPerson:
    def __init__(self):
        self.name = "test name"
        self.age = 10
    def info(self):
        print(f"This is a default constructor. {self.name} is of age {self.age}")

new = newPerson()
new.info()

# 2. Parameterized Constructor - takes arguments along with self
class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a
        print("This is being called")
    def info(self):
        print(f"{self.name} is of {self.age} years old")

a = Person("Avadhoot", 21)
a.info()

b = Person("Test", 20)
b.info()



