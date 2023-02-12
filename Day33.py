# Dictionaries 
# Ordered collection of data items, where each key needs to be unique

dic = {
    "Name": "Avadhoot",
    "LastName": "Bhogil",
    "Age": 23
}

print(dic)
print(dic['Name'])

# when trying to access elements which are not present in the dictionary

# print(dic[43])
print(dic.get(43))

# accessing keys, values and both. 

print(dic.keys())

print(type(dic))

print(type(dic.keys()))

print(dic.values())

print(dic.items())
print(type(dic.items()))

# using for loops.

for key in dic.keys():
    print(f"The value for {key} is:", dic[key])

for i,value in dic.items():
    print(f"the value for {i} is:", value)

