#Quotes Inside Quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#Assign String to a Variable
name = "rawan"
print(name)

#Multiline Strings
statment = """I am a student"""
print(statment)

statment = '''I am a student'''
print(statment)

#Strings are Arrays
print(statment[0] , len(statment))

#Looping Through a String
for char in statment:
    print(char) 

#Check String
shortStatment = "I am a student"
print("student" in shortStatment)

statment = "I like join english class and python class. what classes you like?"
print("class" in statment) #True
print(statment.count("class"))
print(statment.find("class"))
print(statment[20:26])#slice string [start:end]
print(statment[20:])#slice string [start:end]
print(statment[:26])#slice string [start:end]

#Negative Indexing
#Use negative indexes to start the slice from the end of the string
statment = "Hello"
print(statment[-5])#output: "H"

#remove white space
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"