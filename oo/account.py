class Account:
    def __init__(self, number, holder_name, balance, limit=1000.0):
        self.number = number
        self.holder_name = holder_name
        self.balance = balance
        self.limit = limit
