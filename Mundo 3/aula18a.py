galera = [['Vitor', 17], ['João', 18], ['José', 23], ['Ana', 45]]
print(galera[0])
print(galera[0][0])

for c in galera:
    print(f'{c[0]} tem {c[1]} anos.')

pessoas = []
dados = []
for x in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    pessoas.append(dados[:])
    dados.clear()
print(pessoas)

for p in pessoas:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
    else:
        print(f'{p[0]} é menor de idade.')