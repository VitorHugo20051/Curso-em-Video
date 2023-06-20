numeros = []
maior = menor = 0
for c in range(1,6):
    num = int(input('Digite um número: '))
    numeros.append(num)
print(f'Os valores digitados foram {numeros}.')
print(f'O maior valor digitado é {max(numeros)} que foi encontrado nas posições ',end='')
for a, b in enumerate(numeros):
    if b == max(numeros):
        print(f'{a + 1}...',end='')
print()
print(f'O menor valor digitado é {min(numeros)} que se encontra nas posições ',end='')
for a, b in enumerate(numeros):
    if b == min(numeros):
        print(f'{a + 1}...',end='')