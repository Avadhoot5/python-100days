# Single Inheritance 

# It is a type of inheritance where a class inherits properties and behaviors from a single parent class.

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        print("Sound made by the animal")

    
# creating a child class 

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species='Dog')
        self.breed = breed
    
    def make_sound(self):
        print("Bark!")

class Cat(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species='cat')
        self.breed = breed

    def make_sound(self):
        print("Meow Meow")

    def move(self, moving):
        self.moving = moving
        print(f"The {self.name} cat of species {self.species} is currently {self.moving}")

# obj of parent class 
a = Animal('dog', 'doggy')
a.make_sound()

# obj of child class dog 
d = Dog('Doggy', 'husky')
d.make_sound()

# obj of child class cat
c = Cat('catty', 'cutie')
c.make_sound()
c.move('Moving')