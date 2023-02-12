#  dir, __dict__ and help method

'''
We must look into dir(), __dict__() and help() attribute/methods in python. They make it easy for us to understand how classes resolve various functions and executes code. In Python, there are three built-in functions that are commonly used to get information about objects: dir(), dict, and help(). Let's take a look at each of them:

The dir() method
dir(): The dir() function returns a list of all the attributes and methods (including dunder methods) available for an object. It is a useful tool for discovering what you can do with an object.

The __dict__ attribute
__dict__: The __dict__ attribute returns a dictionary representation of an object's attributes. It is a useful tool for introspection. 

The help() mehthod
help(): The help() function is used to get help documentation for an object, including a description of its attributes and methods.

'''
# dir() method
a = [1,2,3]
print(dir(a))

# __dict__ attribute
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person('Avadhoot', 21)
print(p.__dict__)
print(Person.__dict__)

# help() method
help(str)
