class BankAccount:
    # don't forget to add some default values for these parameters!
    bank_name = "WellsDojo"
    all_accounts = []

    def __init__(self, int_rate = 0.05, balance = 0): 
        self.balance =  balance
        self.int_rate = int_rate
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if (self.balance - amount < 0):
            self.balance -= 5
            print("Insufficient funds: Charging a $5 fee")
            return self
        else:
            self.balance -= amount
            return self
    
    def display_account_info(self):
        x = f"Balance: {self.balance}"
        print(x)
        return self
    
    def yield_interest(self):
        if (self.balance > -1):
            self.balance *= self.int_rate
            return self
        else:
            print("N/A")
            return self

jonathan_account = BankAccount()
jason_account = BankAccount()

jonathan_account.deposit(1000).deposit(500).deposit(5000).withdraw(10).yield_interest().display_account_info()
jason_account.deposit(500).deposit(50000).withdraw(2000).withdraw(500).withdraw(3000).withdraw(200).yield_interest().display_account_info()