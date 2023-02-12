# Enumerate Function

# a = [3,15,15,262,634,253,1]

# for k,i in enumerate(a):
#     print(k,i)
#     if k == 4:
#         print("this is the 5th element")


a = [3,15,15,262,634,253,1]

# Changing the start index 

for k,i in enumerate(a,start=1):
    print(k,i)