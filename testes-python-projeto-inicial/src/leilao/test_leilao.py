from unittest import TestCase
from dominio import Usuario, Lance, Leilao


class TestLeilao(TestCase):
    def setUp(self) -> None:
        self.menor_valor_esperado = 100.0
        self.maior_valor_esperado = 150.0

        self.gui = Usuario('Gui')
        self.lance_do_gui = Lance(self.gui, self.maior_valor_esperado)

        self.leilao = Leilao('Celular')

    def setUp_yuri(self, valor):
        yuri = Usuario('Yuri')
        lance_do_yuri = Lance(yuri, valor)

        return yuri, lance_do_yuri

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        yuri, lance_do_yuri = self.setUp_yuri(self.menor_valor_esperado)
        self.leilao.dar_lance(lance_do_yuri)
        self.leilao.dar_lance(self.lance_do_gui)

        self.assertEqual(self.menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(self.maior_valor_esperado, self.leilao.maior_lance)

    def test_nao_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_decrescente(self):
        with self.assertRaises(ValueError):
            yuri, lance_do_yuri = self.setUp_yuri(self.menor_valor_esperado)

            self.leilao.dar_lance(self.lance_do_gui)
            self.leilao.dar_lance(lance_do_yuri)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_o_leilao_tiver_um_lance(self):
        self.leilao.dar_lance(self.lance_do_gui)

        self.assertEqual(self.maior_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(self.maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_menor_lance_quando_o_leilao_tiver_tres_lances(self):
        yuri, lance_do_yuri = self.setUp_yuri(self.menor_valor_esperado)
        outro_lance_do_gui = Lance(self.gui, 90.0)

        self.leilao.dar_lance(outro_lance_do_gui)
        self.leilao.dar_lance(lance_do_yuri)
        self.leilao.dar_lance(self.lance_do_gui)

        self.assertEqual(90.0, self.leilao.menor_lance)
        self.assertEqual(self.maior_valor_esperado, self.leilao.maior_lance)

    # se o leilao não tiver lances, deve permitir propor um lance
    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lances(self):
        self.leilao.dar_lance(self.lance_do_gui)

        quantidade_de_lances_recebidos = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances_recebidos)

    # se o ultimo usuario for diferente, deve permitir propor o lance
    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        yuri, lance_do_yuri = self.setUp_yuri(200)
        self.leilao.dar_lance(self.lance_do_gui)
        self.leilao.dar_lance(lance_do_yuri)

        quantidade_de_lances_recebidos = len(self.leilao.lances)
        self.assertEqual(2, quantidade_de_lances_recebidos)

    # se o o ultimo usuario for o mesmo, não deve permitir propor o lance
    def test_nao_deve_permitir_propror_um_lance_caso_o_ultimo_usuario_seja_o_mesmo_com_fail(self):
        outro_lance_do_gui = Lance(self.gui, 200)

        try:
            self.leilao.dar_lance(self.lance_do_gui)
            self.leilao.dar_lance(outro_lance_do_gui)
            self.fail(msg='Não lançou a exceção')
        except ValueError:
            quantidade_de_lances_recebidos = len(self.leilao.lances)
            self.assertEqual(1, quantidade_de_lances_recebidos)

    def test_nao_deve_permitir_propror_um_lance_caso_o_ultimo_usuario_seja_o_mesmo_com_with(self):
        outro_lance_do_gui = Lance(self.gui, 200)

        with self.assertRaises(ValueError):
            self.leilao.dar_lance(self.lance_do_gui)
            self.leilao.dar_lance(outro_lance_do_gui)
