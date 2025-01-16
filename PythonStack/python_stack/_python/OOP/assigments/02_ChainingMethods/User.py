#Chaining Methods Assignment
class User:
    def __init__(self, name="", email=""):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        if self.account_balance > 0:
           self.account_balance -= amount
           return self
    
    def transfer_money(self, amount, user):
         if self.account_balance > amount:
            self.make_withdrawal(amount)
            user.make_deposit(amount)
            print("User {0} transfer ${1} amount to {2}".format(self.name, amount, user.name))
         else:
             print("No balance to apply transfer ${0} to {1}".format(amount, user.name))
        
    def display_user_balance(self):
        print("User: {0}, Balance:${1}".format(self.name, self.account_balance))
        
#create an instance "OBJECT"
guido  = User("guido", "guido@codingdojo.com")
guido.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance()