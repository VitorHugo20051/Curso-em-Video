number = int(input('Calcular fatorial: '))
c = number
f = 1
print('Calculando {}! = '.format(number))
while c > 0:
    print('{}'.format(c), end=' ')
    f = f * c
    print('x' if c > 1 else '= {}'.format(f), end=' ')
    c -= 1