# Typecasting in Python

# Two types of typecasting - Explicit & Implicit

# Explicit Typecasting

string = "23"
number = 7
string_number = int(string)
sum = string_number + number
print("The sum of both the number is", sum)

# Implicit Typecasting
# python converts lower level data type to a higher level data type, for preventing data loss

a = 2.3
b = 4
print(a+b)
