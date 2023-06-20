núm = soma = count = 0
n1 = int(input('Digite um valor [999 para parar]: '))
while n1 != 999:
    soma += n1
    count += 1
    n1 = int(input('Digite um valor [999 para parar]: '))
print('Você digitou {} números e a soma deles é {}.'.format(count, soma))