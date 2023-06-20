print('Sequencia de Fibonacci')
termos = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end='')
count = 3
while count <= termos:
    t3 = t2 + t1
    print(f' -> {t3} ', end='')
    t1 = t2
    t2 = t3
    count += 1
print('Fim')