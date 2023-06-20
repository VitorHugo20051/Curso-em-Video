from datetime import date
atual = date.today().year
ano = int(input('Ano de nascimento: '))
ida = atual - ano
print('Quem nasceu em {} tem {} em {}.'.format(ano,ida,atual))
if ida > 18:
    tempo = ida - 18
    anos = atual - tempo
    print('Você já devia ser se alistado a {} anos.'.format(tempo))
    print('Seu alistamento foi em {}.'.format(anos))
elif ida < 18:
    tempo = 18 - ida
    anos = atual + tempo
    print('Ainda faltam {} anos para seu alistamento.'.format(tempo))
    print('Seu alistamento será em {}.'.format(anos))
else:
    print('Seu alistamento será este ano.')