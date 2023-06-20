dados = dict()
golos = list()

dados['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))

for i in range(1, partidas + 1):
    dados['golos'] = int(input(f'Quantos golos {dados["nome"]} marcou na partida {i}? '))
    golos.append(dados['golos'])
    dados['aproveitamento'] = golos
    for c in golos:
        dados['total'] = c + c
    del dados['golos']

print('-=' * 20)

print(dados)

print('-=' * 20)

for k, v in dados.items():
    print(f'O campo {k} tem valor {v}.')

print('-=' * 20)

print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')

for a, b in enumerate(golos):
    print(f'Na partida {a + 1} fez {b} golos.')
print(f'Foi um total de {dados["total"]} golos.')