#Functions Intermediate II
x = [[5,2,3] , [10,8,9]]
students = [
    {'first_name': 'Michael' , 'last_name': 'Jordan'},
    {'first_name': 'John' , 'last_name': 'Rosales'},
    {'first_name': 'Mark' , 'last_name': 'Guillen'},
    {'first_name': 'KB' , 'last_name': 'Tonel'}
]

sport_directory = {
    'basketball' : ['Kobe' , 'Jordan' , 'James' , 'Curry'],
    'soccer' : ['Messi' , 'Ronaldo' , 'Rooney']
}

z = [{'x':10 , 'y': 20}] 

#001 Update Values in Dictionaries and Lists
print("#1 Update Values in Dictionaries and Lists")
#1- change value 10 in x to 15
print(f"before: {x}")
x[1][0] = 15
print(f"after: {x}")

#2- change last_name of the first student from 'Jordan' to 'Bryant'
print(f"\nbefore: {students[0]}")
students[0]['last_name'] = 'Bryant'
print(f"after: {students[0]}")

#3- in sport_directory change from 'Messi' to 'Andres'
print(f"\nbefore: {sport_directory["soccer"]}")
sport_directory["soccer"][0] = 'Andres'
print(f"after: {sport_directory["soccer"]}")


#4- change value 20 in z to 30
print(f"\nbefore: {z}")
z[0]["y"] = 30
print(f"after: {z}")

#002 Iterate Through a List of Dictionaries
def iterateDictionary(some_list):
    for item in some_list:
      message_list = [] 
      for key,value in item.items():
          message_list.append("{0} - {1}".format(key, value))
      print(", ".join(message_list)) 

print("\n#02 Iterate Through a List of Dictionaries")
#output format: first_name - KB, last_name - Tonel
iterateDictionary(students)


#003 Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for item in some_list:
        if key_name in item:
          print(item[key_name]) 
        
print("\n#03 Get Values From a List of Dictionaries")
iterateDictionary2("first_name", students)
print("\n")
iterateDictionary2("last_name", students)



#004 Iterate Through a Dictionary with List Values
dojo = {
   'locations': ['San Jose', 'Seattle' , 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh' ,'Devon'],
}

def printInfo(some_dict):
    for key, values in some_dict.items():
       print("\n{0} {1}".format(len(values), key))
       for val in values:
          print(val)
    
        
print("\n#04 Iterate Through a Dictionary with List Values")
printInfo(dojo)

