import random
num = tuple(random.sample(range(10),5))
print(f'Os valores sorteados foram: {num}')
print(f'O maior valor é {max(num)} e o menor é {min(num)}.')
