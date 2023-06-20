from datetime import date
atual = date.today().year
ano = int(input('Em que ano naceste? '))
idade = atual - ano
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Tu é benjamin.')
elif idade <= 14:
    print('Tu és infantil.')
elif idade <= 19:
    print('Tu és junior.')
elif idade <= 25:
    print('Tu és senior.')
else:
    print('Tu es veterano.')