#Intro to OOP
#Using OOP Allow Us to Custamize our data type
#By key word "class" it acts as a templeate
#that templete guarantees the consistent creation of instances


class User:
    #attributes : carecterestic of an object
    #constructor: called when new object instantiated
  
    def __init__(self, name, email_address):
        #self : is the first parameter of every method within a class 
        self.name = name
        self.email = email_address
        self.account_balance = 0
    
    #Methods: actions "functions belong to the class"
    def make_deposit(self, amount):
        self.account_balance += amount
       

#craeting instance of our class
guido = User("Guido van Rossum" , "guido@codingdojo.com")
monty = User("Monty Python" , "monty@codingdojo.com")

guido.make_deposit(300)
monty.make_deposit(50)

print("{0} with balance {1}".format(guido.name, guido.account_balance))
print("{0} with balance {1}".format(monty.name, monty.account_balance))

