class Account:
    def __init__(self, number, holder_name, balance, limit=1000.0):
        self.number = number
        self.holder_name = holder_name
        self.balance = balance
        self.limit = limit

    def check_balance(self):
        print(f"Saldo {self.balance} do titular {self.holder_name}")

    def deposit(self, money):
        money = abs(money)
        self.balance += money

    def withdraw(self, money):
        money = abs(money)
        self.balance -= money
        return money
