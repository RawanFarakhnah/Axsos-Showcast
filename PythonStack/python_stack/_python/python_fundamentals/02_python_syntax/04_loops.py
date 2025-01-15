#python loops
myList = ["apple", "banana", "cherry"]
for x in myList:
    print(x)

print("\n")
[print(x) for x in myList]

print("\n")
newList = myList.copy()
print(newList)

index = 0
while index < len(myList):
    print(myList[index])
    index += 1

print("\n")
for i in range(len(myList)):
    print(myList[i])