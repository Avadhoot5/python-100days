# Recursion 

# It is the process of defining something in terms of itself.
# We know that, a function can call other functins. It is possible for the function to call itself: recursive functions

'''
fact(5) = 5*4*3*2*1
fact(4) = 4*3*2*1
fact(3) = 3*2*1
fact(2) = 2*1

'''

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
print(factorial(3))

# fibonacci series - f(n) = f(n-1)+f(n-2)

def fs(n):
    if(n == 0):
        return 0
    if(n == 1):
        return 1
    else:
        return fs(n-1) + fs(n-2)


print(fs(0))
print(fs(1))
print(fs(2))
print(fs(3))
print(fs(4))
print(fs(5))
print(fs(6))