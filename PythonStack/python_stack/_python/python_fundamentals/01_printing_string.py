#Using Print Method 
import ast


print("Hello World")#output: Hello World

#Using string concatenation + operator
print("Hello" + "World") #output: HelloWorld

#using string multiplication * operator
print("Hello World! "*3)

#printing a new line
print("\n") #output: new line

#Using f-string formatting
name = "rawan"
age = 27
info = f"My name is {name} and I am {age} years old."
print(info) #output: My name is rawan and I am 27 years old.    

#using + operator with string and integer
name = "rawan"
age = 27
info = "My name is " + name + " and I am " + str(age) + " years old." 
print(info) #output: My name is rawan and I am 27 years old.

#using format method
name = "rawan"
age = 27
info = "My name is {} and I am {} years old.".format(name, age)
print(info) #output: My name is rawan and I am 27 years old.


#using format method with index
name = "rawan"
age = 27
info = "My name is {1} and I am {0} years old.".format(age, name)
print(info) #output: My name is rawan and I am 27 years old.

#printing a new line
print("\n") #output: new line

#using % operator
my_favorite_color = "black"
my_favorite_animal = "whale"
my_favorite_place = "beach"
my_favorite_number = 7

info = "My favaorite color is %s, my favaorite animal is %s, \nmy favaorite place is %s, my favaorite number is %d \n" %(my_favorite_color,my_favorite_animal,my_favorite_place,my_favorite_number)
print(info)

#using built-in function repr()
info = repr("Hello World")
print(info) #output: 'Hello World'

#using built-in function eval()
info = eval("10+20")
print(info) #output: 30

#using built-in function str()
info = "We use " + str(10) + "percent of our brain."
print(info)

data = {"name": "rawan", "age": 27 , "job": "developer"}
serialized_data = str(data)
print(serialized_data)
print(type(serialized_data))#output: <class 'str'>

print("\n") #output: new line
#using  most common built-in string functions
greating = "Hello World"
print(greating.upper()) #output: HELLO WORLD
print(greating.lower()) #output: hello world
print(greating.title()) #output: Hello World
print(greating.capitalize()) #output: Hello world
print(greating.swapcase()) #output: hELLO wORLD
print(greating.startswith("HELLO")) #output: False ""case sensitive
print(greating.count("l")) #output: 3
print(greating.find("W")) #output: 6 "character index"
print(greating.index("W")) #output: 6 "character index"
print(greating.replace("World", "Rawan"))#output: Hello Rawan   
print(greating.split()) #output: ['Hello', 'World']
print(len(greating)) #output: 11

