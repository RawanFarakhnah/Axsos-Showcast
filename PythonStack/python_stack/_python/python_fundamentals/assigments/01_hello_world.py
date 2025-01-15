#1. Task: print "Hello World"
print("Hello World") #output: Hello World

#2. Task: print "Hello Rawan!" with name in a variable
name = "Rawan"
print("Hello" , name, "!") #with a comma
print("Hello" + name + "!") #with a + operator

#3. Task: print favarite number
favarite_number = 7
print("My favarite number is", favarite_number) #with a comma
print("My favarite number is " + str(favarite_number)) #with + operator

#4. Task: print the favarite food
favarite_food1 = "mandi"
favarite_food2 = "maglouba"
print("I love to eat {0} and {1}".format(favarite_food1, favarite_food2)) #with .format
print(f"I love to eat {favarite_food1} and {favarite_food2}") # with f f_string
print("I love to eat %s and %s" %(favarite_food1, favarite_food2)) # with f f_string

#5. NINJA BONUS : using some built-in functions

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


