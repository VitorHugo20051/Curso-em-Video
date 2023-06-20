print('Gerador de PA')
p1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termos = p1
count = 1
mais_termos = 10
total = 0
while mais_termos != 0:
    total = mais_termos + total
    while count <= total:
        print('{} -> '.format(termos, end=''))
        termos += r
        count += 1
    print('Pausa')
    mais_termos = int(input('Quantos termos voce quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))