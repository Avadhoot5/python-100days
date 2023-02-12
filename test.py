# List, reversing the list, poping the last element and placing it in the first element of the another list, and compare the first and last list
# this is a DSA topic

# l1 = [25,16,14,34]
# l2 = l1.copy()
# l2.reverse()
# print(l2)
# # print(l2)

# l3 = []

# for i in l2:
#     l3.insert(0,i)

# print(l3)

# fruits = ['apple', 'banana', 'cherry']
# new = []
# for i in fruits:
# 	new.insert(0,i)

# print(new)

# n = int(input("Enter a no to find its sum:"))
# def sumof(n):
# 	sum = 0
# 	for i in range(n):
# 		sum = sum + i
# 	return sum

# print(sumof(3))

n = int(input("Enter a no to find its sum:"))
sum = 0
for i in range(1,n+1):
	sum = sum + i
print(sum)