# While Loops

# i = 0
# while(i<5):
#     print(i)
#     i = i + 1


# Emulate Do while loop in python

i = int(input("Enter a number: "))
print(i)
while(i<=10):
    i = int(input("Enter a number: "))
    print(i)
else:
    print("Done With the Code!")


# decrementing the values

count = 5
while(count>0):
    print(count)
    count = count-1

# Emulate Do while loop in python
# python itself does not support do while loop, so we make while condition true and run it to infinite
# and add a if condition with a break, so the entire loop gets break.

i = 0
while True:
    print(i)
    i = i+1
    if(i%100 == 0):
        break