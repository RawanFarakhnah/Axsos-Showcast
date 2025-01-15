import random
#Python Numbers
x = 1   # int
y = 2.8 #float
z = 1j  #complex

print(type(x))
print(type(y))
print(type(z))

#Integer "positive or negative without decimals or unlimited length"
x = 1 #int
y = 35656222554887711 #int
z = -3255522 #int

#float "positive or negative number with one or more decimals"  
x = 1.10 #float
y = 1.0 #float
z = -25.34 #float
w = 1e3 #float stand for 1 * 10^3

print(w)

#type conversion 
x = 1 #int
y = float(x) #convert from int to float
print(y)

print(random.randrange(1,10)) #random number between 1 to 9