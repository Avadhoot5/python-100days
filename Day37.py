# Finally keyword

# The reason we use finally is, when we are returning something in a function, and if we
# just print the values, that line is not executed, adding finally makes sure that the 
#  specific lines are executed.

# try:
#     l = [1,5,15,14]
#     i = int(input("enter a index: "))
#     print(l[i])
# except:
#     print("some error has occurred")
# finally:
#     print("This gets executed no matter what")

def fun():    
    try:
        l = [1,5,15,14]
        i = int(input("enter a index: "))
        print(l[i])
        return 1
    except:
        print("some error has occurred")
        return 0
    finally:
        print("This gets executed no matter what")

print(fun())