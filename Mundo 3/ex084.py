dados = []
pessoas = []
maior_menor = []
peso = []
maior = ''
menor = ''
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    for c in pessoas:
        for x in c:
            if type(x) is str and x not in maior_menor:
                maior_menor.append(x)
            if type(x) is float and x not in peso:
                peso.append(x)
        maior = maior_menor[peso.index(max(peso))]
        menor = maior_menor[peso.index(min(peso))]
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar in 'N':
        break
print(f'Ao todo as pessoas registadas foram {len(pessoas)}.')
print(f'O maior peso foi de {max(peso)}Kg.Peso de {maior}.')
print(f'O menor peso foi de {min(peso)}Kg.Peso de {menor}.')