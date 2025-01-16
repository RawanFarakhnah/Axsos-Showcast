#Python If , Else Statments

a = 1
b = 2

#called If clouse 
if a < b:
   print("a is less than b")
   print("a is definitely less than b")
print("Not sure if a is less than b")


c = 3
d = 4
if c < d:
   print("c is less than d")
else:
   print("c is Not less than d")
   print("I don't think c is less than d")
print("outside the if block")


e = 7 
f = 8
if e < f: 
    print("e is less than f")
elif e == f:
   print("e is equal to f")
elif e > f + 10:
   print("e is greater than f by more than 10")
else:
   print("e is greater than f")

g = 7
h = 8
if g < h: 
   print("g is less than h")
else:
   if g == h: 
       print("g is equal to h")
   else:
       print("g is greater than h")
