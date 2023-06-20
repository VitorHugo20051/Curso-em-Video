from random import randint
n2 = randint(0,5) # pc vai 'pensar' num numero entre 0 e 5
n1 = int(input('Vou pensar num numero entre 0 e 5. Tente advinhar: ')) # jogador tenta adivinhar esse número
if n1 == n2:
    print('Voce acertou estava pensando no numero {}.'.format(n1)) # consegui acertar o numero
else:
    print('Voce errou.') # não conseguiu