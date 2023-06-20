'''for c in range(1, 11):
    print(c)
print('FIM!')

c = 1
while c < 10:
    print(c)
    c += 1
print('FIM!!!')
c = 1
r = 'S'
while r == 'S':
    c = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('FIM!!')'''
n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:  # só vai fazer o teste para ver se é par ou impar numeros diferentes de 0
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Foram digitados {par} pares e {impar} números ímpares.')
print('Fim')
