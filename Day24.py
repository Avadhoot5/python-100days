# Tuples

tup = (2,52,6,"Hello",True, 25,1,False)
print(type(tup))

# HERE true & false, returns boolean values, when we print the count of 0 or 1, we get an extra count for them as well.

print("The count of 1 is: ", tup.count(1))
print("The count of 0 is: ", tup.count(0))
print(tup.count(2))



# can't add a single item in a tuple, hence need to add a comma after that.
# tup2 = (1)

tup2 = (1,)
print(type(tup2))

# can't update the tuple using indexes, as they are immutable
# tup[3] = 424

# indexs in python
# first_element = tup[1]
# print(first_element)

print(tup[2:4])

# accessing the element using index 

sort = tup.index(2)
print(sort)

# length of tuple

print(len(tup))

# concatenating the tuple.

c = tup + tup2
print(c)
