class BankAccount:


    def __init__(self, int_rate = 0.05, balance = 0): 
        self.balance =  balance
        self.int_rate = int_rate


    def deposit(self, amount):
        self.balance += amount
        return self


    def withdraw(self, amount):
        if (self.balance - amount < 0):
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
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

class User:

    def __init__(self, name):
        self.name = name
        self.account = BankAccount(int_rate=0.02, balance=0)


    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self


    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self


    def display_user_balance(self):
        self.account.display_account_info()
        return self

jeshua = User("Jeshua")
jeshua.make_deposit(1000).make_withdrawal(200).display_user_balance()
