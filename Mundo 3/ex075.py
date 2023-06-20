n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
n4 = int(input('Digite um número: '))
lista = [n1, n2, n3, n4]
tupla = tuple(lista)
print(f'O número 9 apareceu {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3) + 1}ª posição.')
else:
    print('O número 3 não foi digitado.')
for n in tupla:
    if n % 2 == 0:
        print('Os valores digitados pares foram {}.'.format(n,end=''))
