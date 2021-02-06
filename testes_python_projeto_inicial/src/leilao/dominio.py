class Usuario:

    def __init__(self, nome, dinheiro=0):
        self.__nome = nome
        self.__carteira = dinheiro

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira

    def propor_lance(self, leilao: 'Leilao', valor):
        if valor > self.__carteira:
            raise ValueError('Não pode propor um lance com um valor maior que o valor da carteira')

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
        self.maior_lance = 0.0
        self.menor_lance = 0.0

    @property
    def lances(self):
        return self.__lances[:]

    def dar_lance(self, lance: Lance):
        self._validar_lance(lance)

        if not self._tem_lances():
            self.menor_lance = lance.valor
        self.maior_lance = lance.valor

        self.__lances.append(lance)

    def _validar_lance(self, lance: Lance):
        if self._tem_dinheiro(lance.valor):
            raise ValueError('Você só pode dar lances maiores do que já foram dados')

        if self._sao_usuarios_iguais(lance.usuario):
            raise ValueError('O mesmo usuário não pode propror dois lances seguidos')

    def _tem_lances(self):
        return self.__lances

    def _tem_dinheiro(self, valor):
        return self.maior_lance > valor

    def _sao_usuarios_iguais(self, usuario):
        if not self._tem_lances():
            return False

        return usuario == self.__lances[-1].usuario
