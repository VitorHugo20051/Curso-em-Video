print('Gerador de PA')
p1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termos = p1
count = 1
while count <= 10:
    print('{} -> '.format(termos, end=''))
    termos += r
    count += 1
print('FIM!')