# Operator Overloading

class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k
    
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

    def __add__(self, x):
        ''' if we use F-string, the result type will be of string. So we create a vector class'''
        # return f"{self.i + x.i}i + {self.j + x.j}j + {self.k + x.k}k"
        return Vector(self.i + x.i, self.j + x.j, self.k + x.k)
    
    def __sub__(self, x):
        return Vector(self.i - x.i, self.j - x.j, self.k - x.k)

v1 = Vector(1,5,2)
print(v1)
    
v2 = Vector(2,1,9)
print(v2)

print(v1 + v2)
print(type(v1 + v2))
print(v2 - v1)
