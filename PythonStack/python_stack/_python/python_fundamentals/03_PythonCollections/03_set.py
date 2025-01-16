#Python Set
#Unordered, Unchangeable, Unindexed,  No duplicate members
mySet = {1,2,3,4,5,6,7,8,9,10}
mySet.add(11)
print(mySet)

mySet.update([12,13,14,15])
print(mySet)

mySet.add(11) #No Duplicate Members
print(mySet)

#Remove an item
mySet.remove(11)
print(mySet)

#Accessing Set 
for x in mySet:
    print(x)

