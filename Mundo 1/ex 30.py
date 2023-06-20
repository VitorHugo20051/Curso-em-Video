num = int(input('Digite um número: '))
n = num % 2
if n == 0:
    print('O número {} é PAR.'.format(n))
else:
    print('O número {} é ÍMPAR.'.format(n))