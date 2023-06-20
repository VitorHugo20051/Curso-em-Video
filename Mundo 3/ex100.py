import random
from time import sleep
numeros = list()


def sorteia():
    for c in range(0, 5):
        num = random.randint(0, 10)
        numeros.append(num)
    print('Os numéros sorteados foram: ', end='')
    for a in numeros:
        print(f'{a}', end=' ')
        sleep(0.7)


sorteia()


def somapar():
    for x in numeros:
        if not x % 2 == 0:
            numeros.remove(x)
    print(numeros)
    print(f'A soma dos valores pares é {sum(numeros)}.', end='')


somapar()