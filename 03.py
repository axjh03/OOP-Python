# Class and Instance Attributes :
# Now create a new Dog class with a class attribute called .species and two instance attributes called .name and .age:

class Dog:
    species = "Canis Familiaris"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
