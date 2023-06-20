dados = dict()
partidas = list()
equipa = list()
while True:
    dados.clear()
    dados['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    partidas.clear()
    for i in range(1, tot + 1):
        partidas.append(int(input(f'Quantos golos {dados["nome"]} marcou na partida {i}? ')))
    dados['golos'] = partidas[:]
    dados['total'] = sum(partidas)
    equipa.append(dados.copy())

    while True:
        resp = str(input('Quer continuar?[S/N] ')).upper().strip()
        if resp in 'SN':
            break
        else:
            print('Erro.Responda S ou N.')
    if resp == 'N':
        break

print('-' * 30)
print('cod ', end='')
for c in dados.keys():
    print(f'{c:<15}', end='')
print()
for k, v in enumerate(equipa):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 30)

while True:
    busca = int(input('Mostrar dados de qual jogador(999 para parar): '))
    if busca == 999:
        break
    if busca >= len(equipa):
        print(f'Erro.Não existe o valor {busca}!')
    else:
        print(f' -- Levantamento do jogador {equipa[busca]["nome"]}')
        for i, g in enumerate(equipa[busca]["golos"]):
            print(f'    No jogo {i + 1} fez {g} golos.')
        print('-=' * 30)
print('Volte sempre!')