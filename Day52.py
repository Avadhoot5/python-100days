# Lambda functions

multipy = lambda x: x*2
print(multipy(5))

cube = lambda x: x*x*x
avg = lambda x,y,z: (x+y+z)/3

print(cube(4))
print(avg(3,15,16))

# calling function inside function
def apply(fx, value):
    return 30 + fx(value)

print(apply(cube, 2))
print(apply(lambda x: x*x*x*x, 2)) #passing function as an argument

