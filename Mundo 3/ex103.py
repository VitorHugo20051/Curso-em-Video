n = input('Nome do jogador: ')
gol = str(input('Números de golos: '))


def ficha(nome='<desconhecido>', golos=0):
    print(f'O jogador {nome} fez {golos} golo(s) no campeonato.')


if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if n.strip() == '':
    ficha(golos=gol)
else:
    ficha(n, gol)