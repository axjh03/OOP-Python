# Getting Started

# Classes 

# Class: A class is a blueprint for the object for how something should be defined. It itself doesn't have any data inside it. 

# Classes define functions called 'Methods'.

# When something is made from a class, it's called a instance. 

# Syntax :  class ClassName

class Dog:
    pass

# The Dog class isn’t very interesting right now, so let’s spruce it up a bit by defining some properties that all Dog objects should have. There are a number of properties that we can choose from, including name, age, coat color, and breed. To keep things simple, we’ll just use name and age.

# The properties that all Dog objects must have are defined in a method called .__init__().