class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    #deposit method
    def make_deposit(self, amount):
        self.account_balance += amount
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    
    def display_user_balance(self):
        return f"User: {self.name}, Balance: {self.account_balance}"

jonathan = User("Jonathan F. Dimawea", "dimawea@gmail.com")
patrick = User("Nicolas P. Suyat", "suyat@gmail.com")
kian = User("Kian L. Sablad", "sablad@gmail.com")

jonathan.make_deposit(200)
jonathan.make_deposit(1000000)
jonathan.make_deposit(10)
jonathan.make_withdrawal(500000)
print(jonathan.display_user_balance())


patrick.make_deposit(300)
patrick.make_deposit(500000)
patrick.make_withdrawal(20000)
patrick.make_withdrawal(45000)
print(patrick.display_user_balance())

kian.make_deposit(1000)
kian.make_withdrawal(50)
kian.make_withdrawal(20)
kian.make_withdrawal(100)
print(kian.display_user_balance())