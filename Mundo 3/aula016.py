lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim') # tuplas são imutaveis
print(lanche)
print(lanche[1])
print(lanche[3])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-3:])
for c in lanche:
    print(f'{c} -> ',end='')
print('Que bom!')
for c in range(len(lanche)):
    print(lanche[c])
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}.')
print(sorted(lanche)) # vai por em ordem alfabética
print(list(lanche))  # transformou a tupla em uma lista