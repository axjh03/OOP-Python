# Getting Started
# https://realpython.com/python3-object-oriented-programming/ 
# Classes 

# Class: A class is a blueprint for the object for how something should be defined. It itself doesn't have any data inside it. 

# Classes define functions called 'Methods'.

# When something is made from a class, it's called a instance. 

# Syntax :  class ClassName

class Dog:
    pass
print(f"Type : \n{type(Dog())}\n")


# The Dog class isn’t very interesting right now, so let’s spruce it up a bit by defining some properties that all Dog objects should have. There are a number of properties that we can choose from, including name, age, coat color, and breed. To keep things simple, we’ll just use name and age.

# The properties that all Dog objects must have are defined in a method called .__init__().

# __init__() initializes each new instance of the class.

# You can give .__init__() any number of parameters, but the first parameter will always be a variable called self. 

class Dog:
    def __init__(self,name, age):
        self.name = name # creates an attribute called name and assigns to it the value of the name parameter.
        self.age = age # creates an attribute called age and assigns to it the value of the age parameter.
        
# Attributes created in .__init__() are called instance attributes


