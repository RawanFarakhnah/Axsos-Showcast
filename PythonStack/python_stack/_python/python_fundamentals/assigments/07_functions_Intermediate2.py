#Functions Intermediate II
x = [[5,2,3] , [10,8,9]]
students = [
    {'first_name': 'Michael' , 'last_name': 'Jordan'},
    {'first_name': 'John' , 'last_name': 'Rosales'}
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

