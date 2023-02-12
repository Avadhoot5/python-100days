# List Methods

l = [14,34,25,235,1,2,2,1,251,243]
print(l)

# append method - used to add elements to the list 

# l.append(23)
# l.append(32)
# print(l)

# sort method - used to sort the list in the ascending order
# sort(reverse = True) - used to sort the list in descending order
# can't print the list while applying the methods, first apply the method and then print the list

# l.sort()
# print(l)

# l.sort(reverse=True)
# print(l)

# reverse method -  reverses the list

# l.reverse()
# print(l)

# index method - returns the value of the element present at the given index 

# print(l.index(34))

# # count method - prints the number of times an element occurs in the list

# print(l.count(1))

# copy method - used to copy the list 

# l1 = [23,52,35,252,1]
# print(l1)
# m = l1  #here same list is taken as a reference, as the list is stored in l1's memory location, so if we change anything l1 gets changed
# m[0] = 0
# print(l1)

# to avoid any changes in the orginal list, we use copy() method

l1 = [23,52,35,252,1]
print(l1)
m = l1.copy()  #here same list is taken as a reference, as the list is stored in l1's memory location, so if we change anything l1 gets changed
m[0] = 0
print(l1)
print(m)

# Insert Method - used to insert a value at a specific index.

l1.insert(0, 3123)
print(l1)

# extend method - used to open a list and add it in another list's end

l2 = [3,25,2]
m2 = [5,21,53]
l2.extend(m2)
print(l2)

# concatenate method - add two string

a = [23452,52,6,2625]
b = [53,16,262]
c = a+b
print(c)




