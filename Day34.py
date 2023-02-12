# Dictionary Methods

ep = {
    122: 45,
    123: 52,
    352: 52,
    252: 26
}
ep2 = {355:624, 626:252}
ep.update(ep2)
print(ep)

# counting the number of values in a dictionary

# print(len(ep))
# val = ep.keys()
# print(len(val))

# clear the items of a dictionary

# ep.clear()
# print(ep)

empt = {}
print(type(empt))
print(empt)

# pop() - removes the key value pair whose key is passed as the parameter

ep.pop(123)
print(ep)

# popitem() - removes the last k-v pair 

popcatch = ep.popitem()
print(ep)
print(popcatch)

# del - used to delete the dictionary

deleting = {1:3,3:1}

del deleting[1] # used to delete the item using particular key

# del deleting
# deleting.clear()

print(deleting)