from .exceptions import InvalidAmount


class Player:
    def __init__(self, name, money=0):
        self._name = name.strip().lower().title()

        money = int(money)
        if money < 0:
            raise InvalidAmount('O valor de dinheiro tem que ser 0 ou maior')
        self._money = money

    @property
    def name(self):
        return self._name

    @property
    def money(self):
        return self._money

    def add_money(self, money):
        money = int(money)
        if money < 1:
            raise InvalidAmount('O valor a ser adicionado tem que ser maior que 0')

        self._money += money

    def takes_money(self, money):
        money = int(money)
        if money < 1:
            raise InvalidAmount('O valor a ser removido tem que ser maior que 0')

        if money > self._money:
            raise InvalidAmount(f'O valor tem que ser menor do que {self._money}')

        self._money -= money
        return money
