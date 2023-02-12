# Global and Local variables 

x = 5 # Global variable

print(f"global variable before {x}")

def fun():
    y = 9 #local variable
    print(y)
    global x
    x = 23


fun()
print(f"global variable after {x}")
# print(y) throws an error as local variables can't be accessed outside the function. Local variables are created when function is called, and discarded when func. is returned.