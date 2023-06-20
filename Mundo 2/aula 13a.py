n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('FIM')

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')


for c in range(0, 10): # vai ler o valor 10 vezes
    n = int(input('Digite um valor: '))
print('FIM')


s = 0
for c in range(0, 3):
    n = int(input('Digite u valor: '))
    s += n
print('O somatorio desses valores foi {}.'.format(s))