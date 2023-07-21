# Class and Instance Attributes :
# Now create a new Dog class with a class attribute called .species and two instance attributes called .name and .age:

class Dog:
    species = "Canis Familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
dog1 = Dog("Tony", 12)
dog2 = Dog("Fernd", 23)

# You can access the data with the dot (.) notation

print(f"dog1 Name = {dog1.name}")
print(f"dog2 Name = {dog2.name}")

print(f"dog1 Age = {dog1.age}")
print(f"dog2 Age = {dog2.age}")

# Now the Big Thing

print(f"{dog1.species}")
print(f"{dog2.species}")

# everything have same species name 
