# Magic/Dunder Methods
# init method - constructor, gets automatically invoked when an instance of the class is created 

from Day73_emp import Employee

e =  Employee('test')
print(e)
# print(e.name)
# print(len(e))

# if str is not available, it will fall back to repr method
# str method is used to print out an object 
print(str(e))

# repr method is used to get a string representation of an obj. that can be used to recreate the obj.
print(repr(e))

# call method 
calling = e()

# calling the obj 
def new(calling):
    print("this is a method to call obj")
    calling

new(calling)
