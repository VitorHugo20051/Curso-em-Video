nome = str(input('Qual é o seu nome? ')).capitalize().title()
if nome == 'Vitor':
    print('Que nome bonito!')
elif nome == 'Elisa' or nome == 'Tomas':
    print('Belo nome!')
elif nome in 'Rafael Joao Carlos':
    print('Vai estudar')
else:
    print('Seu nome é engraçado!')
print('Tenha um bom dia, {}!'.format(nome))