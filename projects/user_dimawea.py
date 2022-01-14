class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    #deposit method
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        x = f"User: {self.name}, Balance: {self.account_balance}"
        print(x)
        return self
jonathan = User("Jonathan F. Dimawea", "dimawea@gmail.com")
patrick = User("Nicolas P. Suyat", "suyat@gmail.com")
kian = User("Kian L. Sablad", "sablad@gmail.com")

jonathan.make_deposit(200).make_deposit(1000000).make_deposit(10).make_withdrawal(500000).display_user_balance()
patrick.make_deposit(300).make_deposit(500000).make_withdrawal(20000).make_withdrawal(45000).display_user_balance()
kian.make_deposit(1000).make_withdrawal(50).make_withdrawal(20).make_withdrawal(100).display_user_balance()