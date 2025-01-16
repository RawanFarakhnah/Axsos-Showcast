#Functions Basic I
#01 
def a():
    return 5
print(a()) #output 5

#02 
def a():
    return 5
print(a() + a()) #output 10

#03
def a():
    return 5
    return 10
print(a()) #output 5


#04
def a():
    return 5
    print(10)
print(a()) #output 5


#05
def a():
    print(5)
x = a()
print(x) #output None


#06
def a(b,c):
    print(b + c)
#print(a(1,2) + a(2,3)) #output Error

#07
def a(b,c):
   return str(b) + str(c)
print(a(2,5)) #output 25

#08
def a():
   b = 100
   print(b)
   if b < 10:
       return 5
   else:
       return 10
   return 7
print(a()) #output 100,10


#09
def a(b, c):
   if b < c:
       return 7
   else:
       return 14
   return 3
print(a(2,3)) #output 7
print(a(5,3)) #output 14
print(a(2,3) + a(5,3)) #output 21

#10
def a(b, c):
   return b + c
   return 10
print(a(3,5)) #output 8


#11
b = 500
print(b)
def a():
   b = 300
   print(b)
print(b)
a()
print(b) #output 500, 500, 300, 500

#11.2
b = 500
print(b)
def a():
   global b 
   b = 300
   print(b)
print(b)
a()
print(b) #output 500, 500, 300, 300

print("\n")
#12
b = 500
print(b)
def a():
   b = 300
   print(b)
   return b 
print(b)
a()
print(b) #output 500, 500, 300, 500


#13
b = 500
print(b)
def a():
   b = 300
   print(b)
   return b 
print(b)
b = a()
print(b) #output 500, 500, 300, 300



#14
def a():
   print(1)
   b()
   print(2)
def b(): 
    print(3)
a()#output 1,3,2


#15
def a():
   print(1)
   x = b()
   print(x)
   return 10

def b(): 
    print(3)
    return 5

y = a()
print(y) #output 1,3,5,10