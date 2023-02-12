# function arguments

# Default arguments

def avg(a=2, b=4):
    print("The average of two numbers is: ", (a+b)/2)
avg()

# values get override if pass arguments while calling the function. eg. avg(a=4,b=23) OR avg(2) only a is replaced. avg(b=4) b is replaced

# Keyword arguments, like passing the values in form of keys

avg(a=23,b=21)

# Required arguments

# in case if we don't pass arguments in Key value syntax, then it is neccesary to pass the arguments 

def req(a,b):
    print("sum of the two numbers is:", a+b)
req(3,5)

# Variable Length arguments

# *paramater = taken as TUPLE, **paramater = taken as DICTIONARY

def sum(*num):
    print(type(num))
    sum = 0
    for i in num:
        sum = sum + i
    return sum

sumas = sum(4,12,1,5,1,1231,21)
print(sumas)

