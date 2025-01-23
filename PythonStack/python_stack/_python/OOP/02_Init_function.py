#__init__() 
#It is class constructor
#Called automatically every time the class is being used to create a new object
class Person:
    #Use self is a paremeter to reference to the current 
    #instance of the class, and is used to access variables
    #that belong to the class

    #To assign values to object properties,
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #To represent of an object with string
    def __str__(self):
        return f"{self.name}({self.age})"
    
    def displayMessage(self):
        print("Hello my name is " + self.name)

#Create Instance of Class
person1 = Person("Ali", 28)
print(person1)
person1.displayMessage()

#Modify Object Properties
person1.age = 34
person1.displayMessage()

person2 = Person("Ahmad", 28)

#Delete Object Properties
del person1.age
del person1

print(person2)

