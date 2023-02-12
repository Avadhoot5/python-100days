# Instance variables vs Class variables 

# class variable - they are defined at the class level, and are shared among all the instances of the class.
# they are defined outside of any method and are usually used to store information that is common to all instances of the class.

class Employee:
    companyName = 'Microsoft' #defining the class variable
    noOfEmployees = 0
    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.05
        Employee.noOfEmployees += 1
    def showDetails(self):
        print(f'The name of the Employee is {self.name} and the raise amount is {self.raise_amount} in {self.companyName} where there are total {self.noOfEmployees} employees')
    
#creating an instance of the class
a = Employee('Avadhoot')
a.companyName = 'New'
print(a.companyName)
a.showDetails()

b = Employee('Test')
b.companyName = 'tApple'
b.showDetails()

c = Employee('avdoot')
c.showDetails()