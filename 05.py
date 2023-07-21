class Dog():
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name;self.age = age
    def description(self): 
        return f"The name of the dog is {self.name}"
    def printable(self):
        print(f"The age of the dog is {self.age}")
    def speak(self, word:str):
        print(f"{self.name} says {word}")

if __name__ == '__main__':
    dog1 = Dog("Rahul", 10)
    print(dog1.description())
    dog1.printable()
    dog1.speak("Bow Wow")
    
    
# Everything we did we had to call a function to print. But if we want to print let's say the whole object then? we get a error like <__main__.Dog object at 0x00aeff70>
 # Not Helpful!
 
# Eg if I do 
list1 = ["Name1", "Name2", 10, 20]
print(list1)

# But if I do like 

class Cat():
    def __init__(self, name):
        self.name = name
cat1 = Cat("Jeffery")
print(Cat); print(cat1)

# I get a output like this unlike as of the list. 
# <class '__main__.Cat'>
# <__main__.Cat object at 0x10308abf0>

# To tacle this we can handle this with __str__. 
class Cat():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"The name of the cat is {str(self.name)}"

cat1 = Cat("Jeffery")
print(cat1)


# Bascially __str__ is what is returned when not the function but the object is called as a whole