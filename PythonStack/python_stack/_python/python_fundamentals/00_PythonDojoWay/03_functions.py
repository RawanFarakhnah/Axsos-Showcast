#Python Functions
#self code "collection of code"
def function1():
    print("ahhhhhh")
    print("ahhhhhh 2")
print("This is outside the function")

#use this function is to call this function
function1()
function1()

#function can be a mapping
#input or an argument
def function2(x):
    return 2*x


a = function2(3) # return value or output
print(a)

b = function2(4) # return value or output
print(b)

#d = function2() #this will accure an error missing argument x

def function3(x,y):
    return x * y

e = function3(1, 2)
print(e)

#compination 
def function4(x):
    print(x)
    print("still in this function")
    return 3*x

f = function4(4)

def function5(some_argument):
    print(some_argument)
    print("weeeee")

function5(4)