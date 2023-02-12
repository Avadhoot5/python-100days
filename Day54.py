# 'is' vs '==' in Python
# COMPARISON Operators

# is - compares the identity, compares the exact location of object in memory 
# == - compares the value

# constant comparison
a = 6
b = 6

print(a is b) #True
print(a == b) #True

#List comparison
a1 = [1,2,3]
b1 = [1,2,3]

print(a1 is b1) #False - as the lists point to different mem locations.
print(a1 == b1) #True

# tuple comparison
a2 = (1,2,6,4)
b2 = (1,2,6,4)

print(a2 is b2) #True - as tuple can't be changed, so both tuples point to same mem location
print(a2 == b2)


