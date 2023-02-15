# Multiple Inheritance

# It is a powerful feature in OOP that allows a class to inherit attributes & methods from multiple parent classes.
# This can be useful in situations where a class needs to inherit functionality from multiple sources.


class Employee:
    def __init__(self, name):
        self.name = name
    def show(self):
        print(f"The Name is {self.name}")

class Dancer:
    def __init__(self, dance):
        self.dance = dance
    def show(self):
        print(f"The dance is {self.dance}")

class Dancingemployee(Dancer, Employee): #method gets called depending on the order of parent class
    def __init__(self, dance, name):
        self.dance = dance
        self.name = name

o = Dancingemployee('Breakdance', 'loser') 
print(o.name)
print(o.dance)
o.show()

# special method in python - classname.mro() - shows a list of method heirarchy for the obj.

print(Dancingemployee.mro())
