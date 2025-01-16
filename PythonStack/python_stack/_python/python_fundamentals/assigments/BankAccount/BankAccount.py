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

print("First Account")
first_account = BankAccount(balance=1000)
first_account.display_account_info()
first_account.deposit(100).deposit(100).deposit(100).withdraw(50).yield_interest().display_account_info()

print("\nSecond Account")
second_account = BankAccount(int_rate=0.02,balance=500)
second_account.display_account_info()
second_account.deposit(100).deposit(100).withdraw(200).withdraw(200).withdraw(200).withdraw(200).yield_interest().display_account_info()