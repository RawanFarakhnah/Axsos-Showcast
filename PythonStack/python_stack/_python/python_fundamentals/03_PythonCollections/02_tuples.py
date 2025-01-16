#Python Tuples
#Ordered, Unchangeable, indexed,  Allow duplicate members
myTuples = ("apple", "banana", "cherry")
for x in myTuples:
    print(x)

print("\n")


#myTuples[0] = "orange" 
#Error: can not change Tuple value
for x in myTuples:
    print(x)

print("\n")

#unpacking
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

print("\n")

#Using Asterisk*
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)