# Method Overriding

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def area(self):
        return self.x * self.y
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius, radius)
    def area(self):
        return 3.14 * super().area()

# calling the child class, the area classs is modified & overwritten

# parent method 
sh = Shape(5, 5)
print(sh.area())

# calling method 
c = Circle(5)
print(c.area())

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def details(self):
        return f"The Name of the Employee {self.id} is {self.name}"

class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang
    def details(self):
        return f"{super().details()}, and the preffered language is {self.lang}"


emp = Employee('Avadhoot', 23599) 
print(emp.details())

prg = Programmer('Test name', 2352, 'python')
print(prg.details())

