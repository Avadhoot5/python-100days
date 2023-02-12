# Operations on tuple

# Tuples are immutable, hence if we need to add, remove, or change them we need to convert them into list, perform the operations and then convert back to tuple 

countries = ("India", "Finland", "Germany", "Bhutan")
print(countries)
temp = list(countries)
temp.append("Holland")
print(countries)
temp.pop(3)
print(countries)
temp[1] = 'Argentina'
countries = tuple(temp)
print(countries)


# length of the tuple 

test = (3,1,525,1,52,21,1,2,)
print(len(test))

# count method in tuple 

print(test.count(1))

# index in tuple
 
print(test.index(3))

# index of the element using slicing. 
# SYNTAX - tuple.index(element, start, end)

print(test.index(1, 2, 6))

