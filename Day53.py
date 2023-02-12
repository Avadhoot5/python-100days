# Map, Filter and Reduce - Higher Order functions, as they take other functions as arguments

# MAP
# the map func, applies a func to each element in a sequence and returns a new seq. containing the transformed elements

lit = [12,5,1,2,3,7]

# Creating a loop , empty list and then iterating 
# newlit = []
# for i in lit:
#     newlit.append(i*i)
# print(newlit)

mapping = map(lambda x: x*x, lit)
print("Square of the list elements is:", list(mapping))

# def square(x):
#     return x*x
# newmap = map(square, lit)
# print(list(newmap))

# FILTER 
# the filter func, filters a sequence of elements based on a given condition ( a fnc that returns a boolean value) & returns the new seq. of elements that follow the predicate.

def fit(x):
    return x>4

filtering = filter(fit, lit)
print("Filtering the list where elements are greater than 4", list(filtering))


# REDUCE
# the reduce func, returns a final result at the end. 

from functools import reduce

reducing = reduce(lambda x,y: x+y, lit)
print(reducing)