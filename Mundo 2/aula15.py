'''count = 1
while True: # loop infinito
    print(count,'-> ', end='')
    count += 1
print('Acabou')'''

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:   # quando n == 999 ele sai do loop e não soma 999 com outros os numeros
        break
    s += n
print(f'A soma é {s}.')