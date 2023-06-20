def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}.')


somar(2, 3, 5)
somar(8, 4)
somar()


def teste():
    # Variaveis locais
    x = 8
    n = 3
    print(f'Na função teste, n vale {n}.')
    print(f'Na função teste, x vale {x}.')


teste()


# Programa principal
# Variaveis globais
x = 7
n = 2
print(f'No programa principal n vale {n}.')
print(f'Na função teste, x vale {x}.')