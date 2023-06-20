n1 = float(input('Digite a primeira nota : '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('Sua média é {:.1f}.'.format(m))
if m >= 10:
    print('Bom trabalho!!!')
else:
    print('VAI ESTUDAR')