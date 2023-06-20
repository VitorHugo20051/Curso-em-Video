from random import randint
from time import sleep

lista = []
numeros = []
tot = 1
print('Euromilhões')
jogos = int(input('Quantos jogos quer fazer? '))

while tot <= jogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    numeros.append(lista[:])
    lista.clear()
    tot += 1
for i, l in enumerate(numeros):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
print('Boa sorte!')