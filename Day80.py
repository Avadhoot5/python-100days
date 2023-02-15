# Multilevel Inheritance

# It is a type of inheritance in OOP, where a derived class inherits from another derived class
# It allows us to build a heirarchy of classes where one class builds upon another, leading to a more specialized class

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
    
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species = 'Dog')
        self.breed = breed

    def show_details(self):
        Animal.show_details(self)
        print(f"Breed: {self.breed}")
    
class Husky(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed = 'Husky')
        self.color = color
    
    def show_details(self):
        Dog.show_details(self)
        print(f"Color: {self.color}")

ob = Husky('tommy', 'B&W')
ob.show_details()

print(Husky.mro())
