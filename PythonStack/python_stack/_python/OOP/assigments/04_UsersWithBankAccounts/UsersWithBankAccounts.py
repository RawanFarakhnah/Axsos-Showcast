class BankAccount:
    def __init__(self, int_rate=0.01, balance=0): 
        self.int_rate = int_rate
        self.balance = balance
       
    def deposit(self, amount):
        self.balance += amount
        return self
       
    def withdraw(self, amount):
        if self.balance >= amount:
           self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
            
    def display_account_info(self):
        print("Balance: ${0}".format(self.balance))

    def yield_interest(self):
       if self.balance > 0:
          self.balance += self.balance * self.int_rate
       else:
            print("No balance to apply interest to")
       return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {"USD":BankAccount(), "LIS":BankAccount()}
       
    def make_deposit(self, amount , curancy):
        if curancy in self.accounts:
           self.accounts[curancy].deposit(amount)
        else:
           newAccount = BankAccount(balance=amount)
           self.accounts.update({curancy: newAccount})
        return self
    
    def make_withdraw(self, amount , curancy ):
       if curancy in self.accounts:
           self.accounts[curancy].withdraw(amount)
       else:
           print("No Accont with {0} curancy".format(curancy))
       return self
    
    def display_user_balance(self):
        message = "User: {0} have {1} accounts".format(self.name, len(self.accounts)) 
        print(message) 
        for key in self.accounts:
           print("{0} : {1}".format(key, self.accounts[key].balance))
       

first_user = User("Rawan", "rawan@gmail.com").make_deposit(100 , "USD").make_deposit(100 , "JOD").make_deposit(100 , "JOD").make_withdraw(50 , "JOD").make_withdraw(50 , "EUR").display_user_balance()