#Functions Basic II

#01 Countdown 
print("\n#01 Countdown ")
def countdown(num):
   for i in range(num, 0, -1):
      print(i)   
countdown(5)

#02 Print and Return 
print("\n#02 Print and Return")
def print_and_return(myList):
    if len(myList) >= 2:
       print(myList[0])
       return (myList[1])
print_and_return([1,2])

#03 first plus length
print("\n#03 first plus length")
def first_plus_length(myList):
    sum = 0
    if len(myList) > 0:
      sum = myList[0] + len(myList)
    return sum
print(first_plus_length([1,2,3,4,5]))


#04 value greater than second
print("\n#04 value greater than second")
def value_greater_than_second(myList):
   list_of_greater = []
   if len(myList) >= 2:
      second = myList[1]
      for i in range(len(myList)):
          if myList[i] > second:
             list_of_greater.append(myList[i])
   return list_of_greater
         
print(value_greater_than_second([5,2,3,2,1,4]))

#05 This Length, That Value
print("\n#05 This Length, That Value")
def length_and_value(size,value):
    newList = [value] * size   
    return newList

print(length_and_value(size=4,value=7))
print(length_and_value(size=6,value=2))