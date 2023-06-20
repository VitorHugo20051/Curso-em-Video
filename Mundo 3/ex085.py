numeros = []
pares = []
impares = []
for c in range(1,8):
    num = int(input('Digite um número: '))
    numeros.append(num)
for x in numeros:
    if x % 2 == 0:
        pares.append(x)
    else:
        impares.append(x)
print(f'Os valores pares dgitados foram {sorted(pares)}.')
print(f'Os valores impares dgitados foram {sorted(impares)}.')