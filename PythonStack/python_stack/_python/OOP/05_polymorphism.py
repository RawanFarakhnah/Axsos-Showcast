#Python Polymorphism
#Polymorphism "many forms"
#it refers to methods/functions/operators 
#with the same name that can exicuted 
#on many objects or classes

#Polymorphism refers to methods/functions/operators with the same 
#name that can be executed on many objects or classes.


#01- Function Polymorphism
#example len() function , that can be used on 
#different objects 

#String
myStr = "Hello World!"
print(len(myStr))

#Tuple 
myTuple = tuple(("apple", "banana", "cherry"))
print(len(myTuple))

#Dictionary 
myDict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
} 
print(len(myDict))

#02- Class Polymorphism
#Polymorphism is often used in Clss methods
#"When we have multiple class with the same method name"

class Car:
  def __init__(self, brand, model):
      self.brand = brand
      self.model = model
  
  def move(self):
    print("Drive!")

class Boat:
   def __init__(self, brand, model):
      self.brand = brand
      self.model = model
  
   def move(self):
     print("Sail!")

class Plane:
  def __init__(self, brand, model):
      self.brand = brand
      self.model = model
  
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747") 

#Because of polymorphism we can execute 
#the same method for all three classes.
for obj in (car1, boat1, plane1):
    obj.move()


#03- Inheritance Class Polymorphism
#we can use Polymorphism in "classes with child classes"


class Vehicle:#Parent Class
  def __init__(self,brand,model):
     self.brand = brand
     self.model = model
  
  def move(self):
     print("Move!")


class Car(Vehicle):
  pass

class Boat(Vehicle):  
   def move(self):
     print("Sail!")

class Plane(Vehicle):  
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747") 

#Because of polymorphism we can execute
#the same method for all classes.

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()