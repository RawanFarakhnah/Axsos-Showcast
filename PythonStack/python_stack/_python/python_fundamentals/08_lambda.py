#Lambda Function 
from functools import reduce
multiplay = lambda x: x * 2
print(multiplay(2))
print(type(multiplay))


sum = lambda a, b: a + b 
print(sum(2,4))
print(type(sum))

def myfunc(n):
    return lambda a: a * n 

myDoubler = myfunc(4)
print(myDoubler(5))

#1 USE When You Need a Simple Function Temporarily
#If the function is very short and used only once or a few times, using a lambda function can make your code concise.

data = [(1,2), (3,1), (5,4)]
print(data)
#Sorting a list of tuples based on the second value:

data.sort(key = lambda x: x[1])
print(data)

#2. Inline Function for Higher-Order Functions
#Higher-order functions like map, filter, and reduce
nums = [1, 2, 3, 4]
squared = map(lambda x:x ** 2, nums)
print(list(squared))


even_nums  = filter(lambda x:x %2 == 0, nums)
print(list(even_nums))


total = reduce(lambda x, y : x + y, nums)
print(total)

product = reduce(lambda x, y : x * y, nums)
print(product)

#3.When a Short, Inline Function is More Readable
my_dict = {'a': 3, 'b': 1, 'c': 2}
print(my_dict.items())
sorted_items = sorted(my_dict.items(), key=lambda item: item[1])
print(sorted_items)

my_list = ['test_string', 99, lambda x : x ** 2]
print(my_list[2](3))