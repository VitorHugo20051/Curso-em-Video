import operator
import random
from time import sleep

valores = {}
c = 1

print('Valores sorteados:')

for cont in range(1, 5):
    num = random.randint(1, 6)
    valores['jogador' + str(cont)] = num

for k, v in valores.items():
    sleep(0.5)
    print(f'O {k} tirou {v} no dado.')
    sleep(0.5)

print('-=' * 10)
print('Ranking de jogadores:')
print('-=' * 10)

sorte_d = dict(sorted(valores.items(), key=operator.itemgetter(1), reverse=True))
for k, v in sorte_d.items():
    sleep(0.5)
    print(f'{c}º lugar: {k} com {v}.')
    sleep(0.5)
    c += 1