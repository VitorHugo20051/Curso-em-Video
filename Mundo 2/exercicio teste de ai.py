nota = int(input('Qual é a sua nota? '))
if 0 <= nota <= 20:
    if nota >= 10:
        print('Aprovado')
    else:
        print('Reprovado')
else:
    print('Digite um valor entre 0 e 20.') # perguntar ao stor como fazer com que volte a perguntar a nota
