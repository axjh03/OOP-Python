# Instance Methods

class Dog():
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
# Instance methods are functions that are defined inside a class and can only be called from an instance of that class.

    def description(self): # Just like instance attributes, the Instance method's first parameter is also self
        return f"The name of the dog is {self.name}"
    
    def printable(self):
        print(f"The age of the dog is {self.age}")
        
        
    #Another instance method
    def speak(self, word:str): #  variable:DataType  ... Hmmmmm. New thing..
        print(f"{self.name} says {word}")

if __name__ == '__main__':
    dog1 = Dog("Rahul", 10)
    
    # Two ways, but should be coded that way as well. 
    print(dog1.description())
    dog1.printable()
    dog1.speak("Bow Wow")