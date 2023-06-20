from datetime import date

atual = date.today().year
total_maior = 0
total_menor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 18:
        total_maior += 1
    else:
        total_menor += 1
print('O número de pessoas maiores é {}.'.format(total_maior))
print('O número de pessoas menor é {}'.format(total_menor))
