#practice python syntax
#python Indentation
#python Indentation recommanded 4 spaces
if 5 > 2:
    print("Five is greater than two!")

#python Indentation must at least one space
if 5 > 2:
 print("Five is greater than two!")

#1. Variables
# no command for declaring a variable
num1 = 5
greeating = "Hello, World!"

#2. Variable Names
variable = "Hello, World!" #valid
_variable = "Hello, World!" #valid
variable1 = "Hello, World!" #valid
variable_name = "Hello, World!" #valid
Variable = "Hello, World!" #valid
variableName = "Hello, World!" #valid
variableName1 = "Hello, World!" #valid
variable_name_1 = "Hello, World!" #valid
#1variable = "Hello, World!" #invalid
#variable-name = "Hello, World!" #invalid
#variable name = "Hello, World!" #invalid
#1myName = "Hello, World!" #invalid

#name convention
#Camel Case
variableName = "Hello, World!"

#Pascal Case
MyVariableName = "Hello, World!"

#Snake Case
my_variable_name = "Hello, World!"

#3. Assign Value to Multiple Variables
num1 , num2, num3 = 5, 2, 6

#4. Assign one value to Multiple Variables
x = y = z = "Hello, World!"

#4. Output Variables
print(num1)
print(num2)
print(num3)


#change type after assign value
num1 = 5
num1 = "Hello, World!"
print(num1)

#casting
x = str(3)
y = int(3)
z = float(3)
g = complex(3)

print(type(x) ,x)
print(type(y), y)
print(type(z), z)
print(type(g), g)

#case-sensitive : twi defferent variables
name = "Hello, World!"
Name = "Hello, World!"

#Unpack "Destructuring" a Collection
# a list of fruits can be assign to multiple variables "extract" using
# the following syntax

fruits = ["apple", "banana", "cherry"]
fruit1 , fruit2, fruit3 = fruits

#Global Variables
#Variables that are created outside of a function are known as global variables.
#Global variables can be used by everyone, both inside of functions and outside.
#Create a variable outside of a function, and use it inside the function

x = "awesome" #global variable
def myfunc():
   print(f"Python is {x}")

myfunc()

def myfunc2():
   x = "fantastic" #local variable
   print(f"Python is {x}")

myfunc2()

print(f"Python is {x}")

#global keyword
#If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.

def myfunc3():
    global y
    y = "amazing"

myfunc3()
print(f"Python is {y}")

z = "awesome"
def myfunc4():
    global z
    z = "great"
myfunc4()
print(f"Python is {z}") #output : python is great