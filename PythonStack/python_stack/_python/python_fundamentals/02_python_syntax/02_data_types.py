#python data types
#Built-in Data Types
#variables can store data of different types, and different types can do different things.

#Python has the following data types built-in by default, in these categories:
# text type: str
x = "Hello World"
print(type(x) , x)

#numiric type: int,float, complex
x = int(20) 
y = float(20) 
z = complex(20j) 

print(type(x) , x)#output: 20
print(type(y) , y)#output: 20.0
print(type(z) , z)#output: 20j

#sequence type: list, typle, range
x = ["apple", "banana", "cherry"] #list
y = ("apple", "banana", "cherry") #tuple
z = range(6) #range 

print(type(x) , x)#output: ['apple', 'banana', 'cherry']
print(type(y) , y)#output: ('apple', 'banana', 'cherry')
print(type(z) , z)#output: range(0, 6)

#type: dict, set, frozenset
x = {"name" : "John", "age" : 36} #dict
print(type(x) , x)#output: {'name': 'John', 'age': 36}

x = {"apple", "banana", "cherry"} #set
y = frozenset({"apple", "banana", "cherry"}) #frozenset
print(type(x) , x)#output: {'apple', 'banana', 'cherry'}
print(type(y) , y)#output: frozenset({'apple', 'banana', 'cherry'})

#boolean type: bool 
isAlpha = True
isBeta = False
print(type(isAlpha) , isAlpha)#output: True
print(type(isBeta) , isBeta)#output: False

#binary type: bytes, bytearray, memoryview
x = b"Hello"#bytes
print(type(x) , x)

x = bytearray(5)#bytearray
print(type(x) , x[0], x[1], x[2], x[3], x[4])

x = memoryview(bytes(5))#memoryview
print(type(x) , x[0], x[1], x[2], x[3], x[4])

#none type: NoneType
x = None
print(type(x) , x)#output: None
