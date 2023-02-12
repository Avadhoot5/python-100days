# Static Methods 
# static methods are methods that belong to a class rather than a instance of the class 
# They are called on the class itself. DEFINED - @staticmethod decorator

class Math:
    def __init__(self, num):
        self.num = num
    def addton(self, n):
        self.num = self.num + n
    #defining static method, which doesn't requrire self paramater
    @staticmethod
    def add(a, b):
        return a+b
    
#creating an instance of the class
result = Math(2)
print(result.num)
result.addton(3)
print(result.num)

# calling the static method add, using the classname
# no need to create an instance of the class

new = Math.add(12,2)
print(new)

