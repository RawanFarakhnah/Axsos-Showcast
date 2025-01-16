#User Assignment
class User:
    def __init__(self, name, email):
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
first_user  = User("user1", "user1@codingdojo.com")
first_user.make_deposit(800).make_deposit(400).make_deposit(100).make_withdrawal(400).display_user_balance()

second_user = User("user2", "user2@codingdojo.com")
second_user.make_deposit(1000).make_deposit(500).make_withdrawal(400).make_withdrawal(400).display_user_balance()

third_user  = User("user3", "user3@codingdojo.com")
third_user.make_deposit(2500).make_withdrawal(500).make_withdrawal(500).make_withdrawal(300).display_user_balance()

#BONUS
print("\n")
first_user.transfer_money(200, third_user)
first_user.display_user_balance()
third_user.display_user_balance()

print("\n")
first_user.transfer_money(2000, third_user)
first_user.display_user_balance()
third_user.display_user_balance()

