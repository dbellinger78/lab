class Account:
    def __init__(self, acccount_name):
        self.acccount_name = acccount_name
        self.account_balance = 0

    def deposit(self, amount):
        if amount <= 0:
            return False
        elif amount > 0:
            self.account_balance = self.account_balance + amount
            return True
        else:
            return False   

    def withdraw(self, amount):
        if amount <= 0 or amount > self.account_balance:
            return False
        elif amount > 0 and amount < self.account_balance:
            self.account_balance = self.account_balance - amount
            return True
        else:
            return False      
    
    def get_balance(self): 
        return self.account_balance

    def get_name(self):
        return self.acccount_name

