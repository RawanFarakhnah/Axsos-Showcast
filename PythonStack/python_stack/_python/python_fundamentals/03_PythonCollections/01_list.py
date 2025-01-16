#List python 
#Ordered, Changeable, Indexed, Allow duplicate members

myList = [1, 2, 3, 4, 4, 5, 7, 8]
print(len(myList))
print(type(myList))

#list can be of any data type
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]
list4 = [True, False, True, False]

#using list constructor
fruits = list(("apple", "banana", "cherry"))

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

if 0 in myList: 
    print("0 is in the list")


thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

fruits = ", ".join(thislist);
print(fruits)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
#join two lists
list3 = list1 + list2
list4 += list1
for x in list2:
    list4.append(x)

list5 = list1.extend(list2)

print(list3)
list3.clear() #remove all elements

print("\n")
print(list4)
if "a" in list4:
    list4.remove("a")
else:
    pass
 
