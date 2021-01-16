class Player:
    def __init__(self, name, money=0):
        self._name = name.strip().lower().title()
        self._money = money

    @property
    def name(self):
        return self._name

    @property
    def money(self):
        return self._money

    def add_money(self, money):
        self._money += abs(int(money))

    def takes_money(self, money):
        self._money -= abs(int(money))
