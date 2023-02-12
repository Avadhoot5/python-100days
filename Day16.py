# Match Case Statements

# import os 
# print("hello world..")
# os.system("python --version")

# While 

# x = int(input("Enter the value of x: "))
# match x:
#     case 0:
#         print("x is zero")
#     case 4 if x%2==0:
#         print("x%2 == 0 and case is 4")
#     case _ if x<10:
#         print("x is less than 10")

# num = int(input("enter a valid number: "))

# if(num==0):
#     print("The Number is Zero")
# elif(num<0):
#     print("The Number is Negative")
# elif(num>0):
#     print("The Number is Valid")


# num = int(input("enter a valid number: "))

# match num:
#     case 0:
#         print("The Number is Zero")
#     case 1 if (num<0):      # Negative not getting executed
#         print("The Number is Negative")
#     case 2 if (num>0):
#         print("The Number is Valid")
#     case _ if num!=0:
#         print("Please enter a valid number")



num = int(input("enter a valid number: "))

match num:
    case n if (n==0):
        print("The Number is Zero")
    case n if (num<0):
        print("The Number is Negative")
    case n if num>0:
        print("The Number is Valid")
    case _ if num!=0:
        print("Please enter a valid number")