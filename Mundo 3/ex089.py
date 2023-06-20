dados = []

while True:
    nome = (str(input('Nome: ')))
    nota1 = (float(input('Nota 1: ')))
    nota2 = (float(input('Nota 2: ')))
    media = (nota1 + nota2) / 2
    dados.append([nome, [nota1, nota2], media])
    continuar = str(input('Deseja continuar? [S/N]  ')).upper().strip()[0]
    if continuar == 'N':
        break
for i, a in enumerate(dados):
    print(f' {i} Nome: {a[0]}, Média: {a[2]}')

while True:
    opc = int(input('Mostrar notas de qual aluno? (999 para parar) '))
    if opc == 999:
        break
    else:
        print(f'Notas da {dados[opc][0]} são {dados[opc][1]}.')
print('Boa sorte!')