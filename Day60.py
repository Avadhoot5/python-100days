# Getters and Setters

# Getters are methods that are used to access the values of an object's properties. they are used to return the value of a specific property, and are defined as @property decorator

# creating a class MyClass, along with getter & setter
class MyClass:
    def __init__(self, value):
        self._value = value
    # Defining getter
    @property
    def value(self):
        return self._value
    # Defining setter
    @value.setter
    def value(self, new_value):
        self._value = new_value

# Getting the values of the object' properties.
obj = MyClass(12)
print(obj.value)
# Setting the value using setter
obj.value = 23
print(obj.value)

