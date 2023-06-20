lista1 = []
lista_par = []
lista_impar = []

while True:
    num = int(input('Digite um número: '))
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if num not in lista1:
        lista1.append(num)
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)
    if continuar in 'N':
        break
print(f'Os números digitados foram: {lista1}.')
print(f'Os números pares digitados foram: {lista_par}.')
print(f'Os números impares digitados foram: {lista_impar}.')