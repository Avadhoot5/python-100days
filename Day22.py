# Introduction to Lists 

# marks = [1,5,2345,253]
# print(marks)
# print(type(marks))

# for i in marks:
#     if i<270:
#         print(i)
#     else:
#         print("condition not satisfied")

# print(marks[0 :2])

# listname[start:end:jump_index]

list1 = ["hello",3,1,7,8,2,5,21,36]
print(list1[1:7:2])
print(list1[1:8:3])

# Check whether an item is present in the list or not 

if 3 in list1:
    print("Yes exists!")
if 23 in list1:
    print("Yes exists!")
else:
    print("No doesn't exists")

# List comprehensions are used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.

# Syntax:
# List = [Expression(item) for item in iterable if Condition]

list2 = [item for item in range(5)]
print(list2)

list3 = [item for item in range(11) if item%2==0]
print(list3)

list4 = [item*item for item in range(11) if item%2==0]
print(list4)


