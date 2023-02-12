# super keyword 

# the super keyword is used to refer to the parent class. 
# When a class inherits from a parent class, it can override or extend the methods defined in the parent class.
# sometimes, we might wanna use the parent class method in the child class. USE super keyword.

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def parent_method(self):
        print("This is a Method of the Parent Class")

class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang
    def child_method(self):
        print("This is a Method of the Child Class")
        super().parent_method()

emp_1 = Employee('Avadhoot', 23588)
print(emp_1.name, emp_1.id)
emp_1.parent_method()

prg_1 = Programmer('lushactor', 238, 'Python')
print(prg_1.name, prg_1.id, prg_1.lang)
# prg_1.parent_method()
prg_1.child_method()
