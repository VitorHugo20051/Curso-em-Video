matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = 0
soma_terceira = 0
for l in range(0, 3):
    for c in range(0, 3):
        matrix[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[l][c]}]', end='')
    print()
for x in matrix:
    for i in x:
        if i % 2 == 0:
            soma_pares += i
soma_terceira = matrix[0][2] + matrix[1][2] + matrix[2][2]
print(f'A soma dos números pares digitados é {soma_pares}.')
print(f'A soma dos valores da terceira coluna é {soma_terceira}.')
print(f'O maior valor da segunda linha é {max(matrix[1])}.')