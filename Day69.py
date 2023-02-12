# Class Methods

# classes are a way to define custom data types that can store data and define funcs.  that can manipulate data
# class method is a type of method that is bound to the class & not the instance of the class
# @classmethod decorator, followed by a func definition. The 1st argument is always 'cls', which represents the class itself.

class Employee:
    company = 'Apple'
    def show(self):
        print(f"The Name is {self.name} and the company is {self.company}")

    @classmethod
    def changeCompany(cls, newCompany):
        cls.company = newCompany

e1 = Employee()
e1.name = "avadhoot"
e1.show()
e1.changeCompany("Microsoft")
e1.show()
print(Employee.company)