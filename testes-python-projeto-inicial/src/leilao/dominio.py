import sys


class Usuario:

    def __init__(self, nome, dinheiro=0):
        self.__nome = nome
        self.__carteira = dinheiro

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__nome

    def propor_lance(self, leilao: 'Leilao', valor):
        lance = Lance(self, valor)
        leilao.dar_lance(lance)
        self.__carteira -= valor


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = sys.float_info.min
        self.menor_lance = sys.float_info.max

    @property
    def lances(self):
        return self.__lances[:]

    def dar_lance(self, lance: Lance):
        if self.maior_lance > lance.valor:
            raise ValueError('Você só pode dar lances maiores do que já foram dados')

        if self.__lances and lance.usuario == self.__lances[-1].usuario:
            raise ValueError('O mesmo usuário não pode propror dois lances seguidos')

        self.menor_lance = lance.valor if lance.valor < self.menor_lance else self.menor_lance
        self.maior_lance = lance.valor if lance.valor > self.maior_lance else self.maior_lance

        self.__lances.append(lance)
