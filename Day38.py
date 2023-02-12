# Raising custom error

# custom errors are important because if some code does not execute properly due to inital code lines
# we need to create custom errors so that we can allow the proper execution of the program.

# a = int(input("enter a number between 3 and 8: "))


# if(a<3 or a>8):
#     raise ValueError("Number is not between 3 and 8")


# if user writes quit , no error should be displayed,
# but if user writes another string the error should be displayed

# Rasing error if string is not quit
# val = input("enter any word: ")
# if(val != 'quit'):
#     raise ValueError(f"invalid literal for int with base 10: {val} ")

# n = input("Enter a number between 3 and 8: ")

# try:
#     if((int(n)<3) or (int(n)>8)):
#         raise ValueError("no not in the range")
# except:
#     if((str(n) != 'quit')):
#         raise ValueError("invalid string")

a = input("Enter any number between 5 & 9: ")

if(a == "quit"):
    pass
elif(int(a)<5 or int(a)>9):
  raise ValueError("Value should be between 5&9") 
