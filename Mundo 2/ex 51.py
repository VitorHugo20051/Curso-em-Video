b1 = '=' * 20
print(b1)
print('10 TERMOS DE UMA PA')
print(b1)
p1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = p1 + (10 - 1) * razao
for c in range(p1, decimo + razao, razao):
    print(c, end=' -> ')
print('ACABOU')