lista = []

while True:
    num = int(input('Digite um número: '))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado...')
    else:
        print('Valor duplicado, não foi adicionado...')
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if continuar.isnumeric():
        print('Valor inválido.Tente novamente!')
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    elif continuar == 'N':
        break
print(f'Os número digitados foram {sorted(lista)}.')