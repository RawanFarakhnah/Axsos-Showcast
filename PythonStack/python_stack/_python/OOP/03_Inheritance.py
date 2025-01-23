#Python Inheritance
#Inheritance allow us to define a class that 
#inherits all the methods and properities 
#from another calss

##Parent class : (base class) class being to inherited from
##Child class: (derived class) class that inherits from another class

#Create a Parent Class
## Any class can be a parent class
## Sentax is the same as creating any other class

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printName(self):
        print(self.fname, self.lname)
    
#Create a Child Class
#To create a class that inherits the functionality 
#from another class, send the parent class as a 
#parameter when creating the child class:

#Use the Person class to create an object, 
#and then execute the printname method:
person1 = Person("John", "Doe")
person1.printName()

#Use the pass keyword when you do not want to add
#any other properties or methods to the class.
#Use pass keyword to avoid getting an error
class Teacher(Person):
    pass

class Student(Person):
  def __init__(self, fname, lname, year): #no longer child inherite parent Init function
      #Person.__init__(self, fname, lname) ##kept the inheritance of the parent class
      super().__init__(fname, lname)
      self.graduationyear = year

  def welcome(self):
      print("Welcome", self.fname, self.lname, "to the class of", self.graduationyear) 
       

student1 = Student("Mike", "Olsen", 2019)
student1.printName()
student1.welcome()


