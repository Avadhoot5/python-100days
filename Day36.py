# Exception Handling

# a = (input("enter a number:"))
# print(f"Multiplication table of {a} is")

# try:
#     for i in range(1,11):
#         print(f"{int(a)} X {i}: {int(a)*i}")
# except Exception as e:
#     print(e)

# print("Remaining lines of code")


try:
    num = int(input("Enter any integer value:"))
    a = [2,52,215,25]
    print(a[num])
except IndexError:
    print("index error occurred")
except ValueError:
    print("Number is not an integer:")

print("Remaining lines of code")
