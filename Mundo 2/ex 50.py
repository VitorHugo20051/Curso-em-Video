count = 0
soma = 0
for c in range(1, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        count = count + 1
        soma += num
print('A soma dos {} números pares lidos é {}.'.format(count, soma))