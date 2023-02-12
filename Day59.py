# Decorators 

# A decorator is a function that takes another func. as an argument and returns a new func. that modifies the behavior of the orginial func.

def decor(fx):
    def mfx(*args, **kwargs):
        print("This is the start of the function")
        fx(*args, **kwargs)
        print("Function is ending!")
    return mfx

# @decor
# def hello():
#     print("Hello World")

# new = decor(hello)()
# decor(func as an argumet)(call/run the function)

@decor
def add(a,b):
    print(a+b)

adding = add(23,42)
# adding_1 = decor(add)(23,42)

import logging

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a + b

fun = my_function(2,4)
print(fun)