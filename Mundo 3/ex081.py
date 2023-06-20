lista = []
cont = 0

while True:
    num = int(input('Digite um valor: '))
    cont += 1
    lista.append(num)
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
lista.sort(reverse= True)
print(f'Foram digitados {cont} números.')
print(f'A os números em ordem decrescente: {lista}.')
if 5 in lista:
    print('O número 5 está presente.')
else:
    print('O número 5 não está presente.')