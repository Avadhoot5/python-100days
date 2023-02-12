# Set Methods 

a = {'Delhi', 'Pune', 'Mumbai', 'Chennai'}
b = {'Mumbai', 'Kolkata', 'Bangalore', 'Pune'}

print(a,b)

# prints all the value items of both set 

# unionofab = a.union(b)
# print(unionofab)
a.update(b)
print(a)

# prints the common values of both set

c = {'Delhi', 'Pune', 'Mumbai', 'Chennai'}
d = {'Mumbai', 'Kolkata', 'Bangalore', 'Pune'}

print(c,d)

# intersectionof = c.intersection(d)
# print(intersectionof)

c.intersection_update(d)
print(c)

# Symmetric difference and s_d_update()
# sd = union - intersection // prints the values that are not common 

e = {'Delhi', 'Pune', 'Mumbai', 'Chennai'}
f = {'Mumbai', 'Kolkata', 'Bangalore', 'Pune'}

# sd = e.symmetric_difference(f)
# print(sd)

e.symmetric_difference_update(f)
print(e)

# difference method A-B

g = {'Delhi', 'Pune', 'Mumbai', 'Chennai'}
h = {'Mumbai', 'Kolkata', 'Bangalore', 'Pune'}
g.difference_update(h)
print(g)

# isdisjoint() - checks if items of given set are present in another set.

i = {'Delhi', 'Pune3', 'Mumbai2', 'Chennai'}
j = {'Mumbai', 'Kolkata', 'Bangalore', 'Pune'}
print(i.isdisjoint(j))

# issuperset() - checks if all the items of a particular set are present in the original set 
# issubset() - checks if all the items of the original set are present in the particular set

cities = {'tokyo', 'madrid', 'berlin', 'delhi'}
cities2 = {'tokyo', 'madrid'}
print('Is cities superset of cities2', cities.issuperset(cities2))
print('Is cities 2 subset of cities', cities2.issubset(cities))

# SET METHODS

# add() - adds a single item to the set 

adding = {2,5,22,42,'dad'}
adding.add(234)
print(adding)

# remove()/discard() - remove throws an error/ discard does not throw an error while trying to delete and item not
# present in the list

# adding.remove(2)
# adding.discard(5)
# print(adding)

# pop() - removes the last element from the set, as set is unordered, random value gets popped, 
# we can catch that value by storing it to a variable

catching = adding.pop()
print(catching)

# del - it is a keyword which is used to delete the entire set.
# clear() - clears the items in the set and prints an empty set

test = {1,151,15,167,7,'af'}

# del test

# test.clear()

print(test)

# IN keyword to check if a value is present in the set. 

if 1 in test:
    print("present")
else:
    print("not present")