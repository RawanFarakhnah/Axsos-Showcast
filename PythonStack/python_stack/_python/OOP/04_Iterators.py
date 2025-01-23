#Python Iterators
#iterator is an object that contains a countable number of values
#(tuple, set, list, dict) even string are iterable objects

my_tuple = ("apple","banana", "cherry")
my_iter = iter(my_tuple)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

my_str = "banana"
my_iter = iter(my_str)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

#Looping Through an Iterator
for item in my_tuple:
    print(item)

for item in my_str:
    print(item)

#Loop actually creates an iter iterator object 
#and executes the next() method for each loop.