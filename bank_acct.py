class BankAccount():
#don't forget to add some default values for these parameters!
    

    def __init__(self, account_bal = 0,interest_rate = .02):
        self.interest_rate = interest_rate
        self.account_bal = account_bal
        self.account_bal = account_bal
        self.interest_rate = interest_rate
        

    def deposit(self,amount):
        self.account_bal += amount
        return self

    def withdraw(self,amount):
        self.account_bal -= amount
        if(self.account_bal < 0):
            print("Insufficient funds: Charging a $5 fee!")
            self.account_bal -= 5
        return self

    def display_account_info(self):
        return print(self.account_bal)

    def yield_interest(self):
        self.account_bal *= (self.interest_rate +1)
        return self


John = BankAccount()
Drake = BankAccount()


John.deposit(100).deposit(400).deposit(800).withdraw(105).yield_interest().display_account_info()

Drake.deposit(300).deposit(200).withdraw(50).withdraw(50).withdraw(50).withdraw(50).yield_interest().display_account_info()