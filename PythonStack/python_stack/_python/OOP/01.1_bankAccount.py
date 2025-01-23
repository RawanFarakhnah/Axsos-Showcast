class BankAccount:
    def __init__(self, int_rate=0.01, balance=0): 
        self.int_rate = int_rate
        self.balance = balance
    
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

class RetirementAccount(BankAccount):
    def __init__(self, int_rate=0.01, is_roth=False, balance=0): 
       super().__init__(int_rate, balance)
       self.is_roth = is_roth

    def withdraw(self, amount, is_early):
        if is_early:
           amount *= 1.10
        if self.balance >= amount:
           self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
class CheckingAccount(BankAccount):
    def __init__(self, int_rate=0.01, balance=0): 
        super().__init__(int_rate, balance)
    
    def withdraw(self, amount):
        if self.balance >= amount:
           self.balance -= amount
        else:
            print("Insufficient funds")
            
        return self