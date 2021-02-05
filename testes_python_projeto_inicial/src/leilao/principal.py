from testes_python_projeto_inicial.src.leilao.dominio import Usuario, Lance, Leilao

gui = Usuario('Gui')
yuri = Usuario('Yuri')

lance_do_yuri = Lance(yuri, 100.0)
lance_do_gui = Lance(gui, 150.0)

leilao = Leilao('Celular')

leilao.dar_lance(lance_do_yuri)
leilao.dar_lance(lance_do_gui)

for lance in leilao.lances:
    print(f'O usuario {lance.usuario.nome} deu um lance de {lance.valor}')

print(f'O maior lance foi de {leilao.maior_lance}')
print(f'O menor lance foi de {leilao.menor_lance}')