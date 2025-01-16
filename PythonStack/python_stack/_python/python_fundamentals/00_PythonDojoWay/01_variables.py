#Imagine Variables as Pointeres in python 
print("Hello World!")
print('Other String!')
print(3)

#Get To Know more In Variables
a = 1 #a pointing on 1
b = 2 #b pointing on 2
c = "hello there" #c pointing on "hello there"

b = 1 #b pointing on 1
b = "ahhhhhhhhh" #b pointing on "ahhhhhhhhh"

#print(e) #Error e not defined yet
e = 5 #e pointing on 5
print(e) #this works

d = "hello!!" #d pointing on "hello!!"
f = e #f pointing on value of e which is 5
e = 10

print((f"f is {e}")) #output 10
print(f"f is {f}") #output 5