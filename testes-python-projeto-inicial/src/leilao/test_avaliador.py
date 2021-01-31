from unittest import TestCase
from dominio import Usuario, Lance, Leilao


class TestAvaliador(TestCase):
    def setUp(self) -> None:
        self.menor_valor_esperado = 100.0
        self.maior_valor_esperado = 150.0

        self.gui = Usuario('Gui')
        self.lance_do_gui = Lance(self.gui, self.maior_valor_esperado)

        self.leilao = Leilao('Celular')

    def setUp_yuri(self) -> None:
        self.yuri = Usuario('Yuri')
        self.lance_do_yuri = Lance(self.yuri, self.menor_valor_esperado)

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        self.setUp_yuri()
        self.leilao.dar_lance(self.lance_do_gui)
        self.leilao.dar_lance(self.lance_do_yuri)

        self.assertEqual(self.menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(self.maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_decrescente(self):
        self.setUp_yuri()
        self.leilao.dar_lance(self.lance_do_yuri)
        self.leilao.dar_lance(self.lance_do_gui)

        self.assertEqual(self.menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(self.maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_o_leilao_tiver_um_lance(self):
        self.leilao.dar_lance(self.lance_do_gui)

        self.assertEqual(self.maior_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(self.maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_menor_lance_quando_o_leilao_tiver_tres_lances(self):
        self.setUp_yuri()
        outro_lance_do_gui = Lance(self.gui, 120.0)

        self.leilao.dar_lance(self.lance_do_yuri)
        self.leilao.dar_lance(self.lance_do_gui)
        self.leilao.dar_lance(outro_lance_do_gui)

        self.assertEqual(self.menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(self.maior_valor_esperado, self.leilao.maior_lance)