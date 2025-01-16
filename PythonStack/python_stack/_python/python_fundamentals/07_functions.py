#functions
#A function is a block of code which only runs when it is called.

#create a function
def my_function():
    print("Hello from a function")

my_function()

#arrgumsents in function
def my_function(fname):
    print(fname)

my_function("Ali")

#Arbitrary Arguments, *args
def my_function(*kids):
    print(kids)

my_function("Emil", "Tobias", "Linus") 

#Keyword Arguments
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus") 

def my_function(x ,/):
    print(x)

my_function(3)#valid
#my_function(x = 3) #not valid
