# If Else Conditional Statements

a = int(input("Enter your age: "))
print("Your age is: ", a)

if(a>18):
    print("You are eligible to drive")
else:
    print("You are not eligible to drive")

# elilf statement

#the condition gets checked from start to end. if the condition gets satisfied at start
#the program skips the conditions below it and returns the ans for satisfied condition

num = int(input("Enter the value of a number: "))
if(num<0):
    print("The Number is Negative")
elif(num == 0):
    print("The Number is Zero")
else:
    print("The Number is Positive")

# Nested If else statement

# nesting multiple if else elif statements inside each other.
# Level Of Indents are there in nested if else statements. EG. 1st condition 1st LOI, 2nd conditon if inside any if/elif statement, then it is 2nd LOI.

number = int(input("Enter a number: "))
if(number<0):
    print("The Number is Negative")
elif(number>0):
    if(number<10):
        print("The Number is less than 10")
    elif(number>=10 and number<=20):
        print("The Number is between 10-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is Zero")


        