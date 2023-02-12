# Functions

# example

# a = input
# b = input
# mean1 = (a*b)/(a+b)
# print(mean1)

# c = input
# d = input
# mean2 = (c*d)/(c+d)
# print(mean2)

# repeating the code on and on for performing one task does not makes sense, so we use FUNCTIONS

a = int(input("Enter a number: "))
b = int(input("Enter b number: "))
def Gmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)
    greater(a, b)

def greater(a, b):
    if a==b:
        print("both are equal")
    elif a>b:
        print(a, "is greater")
    else:
        print(b, "is greater")

Gmean(a, b) # calling a function

# if you want to complete a function later, but just needs to be added in the code use PASS

def testfun(a, b):
    pass


