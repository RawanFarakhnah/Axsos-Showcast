#List in Python
#assign variables to a
a = [3, 6, -1]
print(a)

#adding an item to the list 
a.append(1) #adding to the end
print(a)
a.insert(0 , 5) #adding an item in special index
print(a)

a.append("hello")
print(a)

a.append([1,3])
print(a)

#delete an item in list
a.pop()#delete last item
print(a)

#accessing item and update it is values
print("first item is", a[0])
print("fourth item is", a[3])

a[0] = 20
a[3] = 22
print("first item is", a[0])
print("fourth item is", a[3])

