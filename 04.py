# Instance Methods

class Dog():
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
# Instance methods are functions that are defined inside a class and can only be called from an instance of that class.

    def description(self): # Just like instance attributes, the Instance method's first parameter is also self
        return f"The name of the dog is {self.name}"
        
dog1 = Dog("Jimmy", 20)
print(dog1.description)