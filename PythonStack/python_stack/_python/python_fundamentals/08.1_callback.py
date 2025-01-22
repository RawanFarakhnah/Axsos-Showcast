#Callback Function 
#When one function is called from another function it is known as a callback
#Callback Function is a function that passed as an argument to another 
#### It can be done in two ways:
  ## Passing one function as an argument to another function
  ## Calling a function inside another function

#Example 
#Syntax: sorted(iterable, key)
## iterable data structure that is to be sorted
## key Criteria for sorting
### calling key function INSIDE the sorted function. 
#The key function here is callback 

#Callback in built-in functions
myList = ["lmn", "AbCd", "khJH", "ert", "SuNnY"]
print(sorted(myList))
print(sorted(myList, key = str.lower ))

#Callback in user-defined functions 

def called(n):
    return n[0] * n[1]

def caller(func, n):
    return func(n)

num = (8,5)
ans = caller(called, num)
print("Multiplication =", ans)

def invoker(callback):
    print(callable(2))

invoker(lambda x: 2* x)