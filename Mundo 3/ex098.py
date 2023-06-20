from time import sleep


def contador():
    print('-=' * 20)
    print('Contagem de 1 a 10 de 1 em 1:')
    for c in range(1, 11):
        sleep(0.5)
        print(f'{c}', end=' ')
    print('Fim')
    print('-=' * 20)
    for i in range(10, -2, -2):
        sleep(0.5)
        print(f'{i}', end=' ')
    print('Fim!')
    print('-=' * 20)
    print('Agora é a sua vez de personalizar a sua contagem!')
    inicio = int(input('Inicio: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    for a in range(inicio, fim, passo):
        print(f'{a}', end=' ')
    print('Fim!')


contador()