# For Loops

# Sometimes, a programmer wants to execute a group of statements a certain number of times.

name  = "Avadhoot"
for i in name:
    print(i)

# Iterating over a list
#nesting for inside a for loop

colors = ["red", "green", "blue", "yellow"]
for color in colors:
    print(color)
    for i in color:
        print(i)

# Range in python

for k in range(10):
    print(k)

for k in range(3,11):
    print(k+1)

for k in range(3,12,2):
    print(k)

# multiplying a number

num = int(input("Enter a number to Multiply: "))
for i in range(1,11):
    print(i*num)

# decrementing the values

for i in range(10,1,-1):
    print(i)