from datetime import datetime


def voto():
    ano_nascimento = int(input('Em que ano você nasceu? '))
    ano_atual = datetime.today().year
    idade = ano_atual - ano_nascimento
    if 17 <= idade < 18 or idade > 70:
        print(f'Com {idade} anos: Voto opcional.')
    elif 18 <= idade <= 70:
        print(f'Com {idade} anos: Voto obrigatório.')
    elif idade < 17:
        print(f'Com {idade} anos: voto negado.')


voto()