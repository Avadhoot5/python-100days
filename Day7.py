# Exercise 1: Calculator using Python 

#operators in python
# 1. Arithmetic operators
'''
print(15+7)
print(6-2)
print(3*2)
print(3**3)
print(7/3)
print(7%5)
print(8//3)
'''

# Develop a calculator of performing add,sub,multi,divide,modulo,floor div. And provide output in a readable manner.

a = int(input("Enter first number to perform arithmetic operations: "))
b = int(input("Enter second number to perform arithmetic operations: "))
add = a+b
sub = a-b
multiply = a*b
divide = a/b
power = a**b
remainder = a%b
floordiv = a//b
print("Addition of",a,"and",b,"is:",add)
print("Subtraction of",a,"and",b,"is:",sub)
print("Multiplication of",a,"and",b,"is:",multiply)
print("Division of",a,"and",b,"is:",divide)
print("Power of",a,"to",b,"is:",power)
print("Remainder of",a,"when divided by",b,"is:",remainder)
print("Integer Division for",a,"and",b,"is:",floordiv)