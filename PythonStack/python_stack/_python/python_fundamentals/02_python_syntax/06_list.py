#python list
myEmptyList = [] #empty list
print(myEmptyList)

del myEmptyList #delete list
#print(myEmptyList) #Error: name 'myEmptyList' is not defined

myList = ["apple", "banana", "cherry"]
for x in myList:
    print(x)    

print("\n")
[print(x) for x in myList]

myList.insert(1,"orange") #insert at index 1
myList.append("mango") #append at the end
myList.remove("banana") #remove by value
myList.pop() #remove last element
print(myList)

myList.pop(0) #remove first element
print(myList)

myList = [1,2,3]
sortedList = sorted(myList,reverse = True) #Returns a new sorted list
print(sortedList) # [3, 2, 1]

myList.sort() #sort ascending in place
print(myList)
