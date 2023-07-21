# Class Attributes : You can define a class attribute by assigning a value to a variable name outside of .__init__().

# All Dog objects have a name and an age, but the values for the name and age attributes will vary depending on the Dog instance.

# On the other hand, class attributes are attributes that have the same value for all class instances. You can define a class attribute by assigning a value to a variable name outside of .__init__().


# Class attributes are defined directly beneath the first line of the class name


class Dog:
    # Class attributes
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

# In this code, you create two new Dog objects and assign them to the variables a and b. When you compare a and b using the == operator, the result is False. Even though a and b are both instances of the Dog class, they represent two distinct objects in memory.

a = Dog("Robert", 10) # Python essentially removes the self parameter, so you only need to worry about the name and age parameters.
b = Dog("Robert", 10)

print(a == b) # Returns False 
# they represent two distinct objects in memory. although they are assigned as same. 
