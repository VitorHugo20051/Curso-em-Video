import random
from time import sleep
bunito = 12*'-='
print('Baza jogar pedra, papel ou tesoura.')
print('Suas opções:')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')
opção = int(input('Qual é a tua jogada? '))
print('PEDRA')
sleep(1)
print('PAPEL')
sleep(1)
print('OU TESOURA!!!')
lista = [0, 1, 2]
pc = random.choice(lista)
if opção == pc:
    if opção == 0:
        print(bunito)
        print('O PC escolheu PEDRA\nO jogador escolheu PEDRA')
        print(bunito)
    elif opção == 1:
        print(bunito)
        print('O PC escolheu PAPEL\nO jogador escolheu PAPEL')
        print(bunito)
    elif opção == 2:
        print(bunito)
        print('O PC escolheu TESOURA\nO jogador escolheu TESOURA')
        print(bunito)
    print('EMPATE!')
elif pc == 0 and opção == 1:
    print(bunito)
    print('O PC escolheu PEDRA\nO jogador escolheu PAPEL')
    print(bunito)
    print('O jogador VENCEU!')
elif pc == 0 and opção == 2:
    print(bunito)
    print('O PC escolheu PEDRA\nO jogador escolheu TESOURA')
    print(bunito)
    print('O JOGADOR PERDEU!')
elif pc == 1 and opção == 0:
    print(bunito)
    print('O PC escolheu PAPEL\nO jogador escolheu PEDRA')
    print(bunito)
    print('O JOGADOR PERDEU!')
elif pc == 1 and opção == 2:
    print(bunito)
    print('O PC escolheu PAPEL\nO jogador escolheu TESOURA')
    print(bunito)
    print('O jogador VENCEU!')
elif pc == 2 and opção == 0:
    print(bunito)
    print('O PC escolheu TESOURA\nO jogador escolheu PEDRA')
    print(bunito)
    print('O JOGADOR VENCEU!')
elif pc == 2 and opção == 0:
    print(bunito)
    print('O PC escolheu TESOURA\nO jogador escolheu PEDRA')
    print(bunito)
    print('O JOGADOR VENCEU!')
elif pc == 2 and opção == 1:
    print(bunito)
    print('O PC escolheu TESOURA\nO jogador escolheu PAPEL')
    print(bunito)
    print('O JOGADOR PERDEU!')