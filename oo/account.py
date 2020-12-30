class Account:
    def __init__(self, number, holder_name, balance, limit=1000.0):
        self.__number = number
        self.__holder_name = holder_name
        self.__balance = balance
        self.__limit = limit

    def check_balance(self):
        print(f"Saldo {self.__balance} do titular {self.__holder_name}")

    def deposit(self, money):
        money = abs(money)
        self.__balance += money

    def withdraw(self, money):
        money = abs(money)
        self.__balance -= money
        return money

    def transfer(self, money, target_account: 'Account'):
        self.withdraw(money)
        target_account.deposit(money)
