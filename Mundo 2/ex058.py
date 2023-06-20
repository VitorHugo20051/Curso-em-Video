import random

tentativas = 0
print('Sou seu computador...')
print('Acabei de adivinhar em um número entre 0 e 10.')
print('Será que consegues adivinhar qual foi?')
palpite = int(input('Qual é o teu palpite? '))
lista = [0,1,2,3,4,5,6,7,8,9,10]
numero = random.choice(lista)

while palpite != numero:
    if palpite > numero:
        palpite = int(input('Menor... Tente mais uma vez.'))
    if palpite < numero:
        palpite = int(input('Maior... Tente mais uma vez.'))
    tentativas += 1
print('Acertaste com {} tentativas.Parabéns!'.format(tentativas))