# Access Modifiers 

# public, private, protected A.M.

class Student:
    def __init__(self, age, name):
        self.age = age #public variable
        self.name = name #public variable

#public var, can be accessed from anywhere
obj = Student(20,'Hello')
print(obj.name)

# private am.
# Name Mangling - it is a technique used to protect the class-private & superclass-private attributes from being accidentally overwritten by sublasses.
# accessing private members, object_name._ClassName__method/attribute_name
class Employee:
    def __init__(self, age, name):
        self.__age = age
        self.__name = name
emp = Employee(30,'Testing')
# print(emp.__age) # Cannot be accessed directly
# print(emp.__dir__()) # dir - to print all the methods used on class Employee
print(emp._Employee__age)


# Protected A.M. this is just a naming covention, it does not actually provide any protection or restrict access to the member.
