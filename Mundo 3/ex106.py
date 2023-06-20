from time import sleep


def ajuda():
    while True:
        comando = str(input('Biblioteca ou função: ')).strip().lower()
        if comando == 'fim':
            print('Programa encerrado!')
            break
        print(f'Acessando manual de {comando}.')
        sleep(1.0)
        print(f'{help(comando)}')


ajuda()