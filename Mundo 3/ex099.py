from time import sleep


def maior(*num):
    print('-=' * 23)
    numeros = list(num)
    sleep(0.6)
    print('Analisando os valores passados...')
    sleep(0.6)
    for a in numeros:
        print(f'{a}', end=' ')
        sleep(0.75)
    sleep(0.5)
    print(f'Foram informados {len(numeros)} valores ao todo.')
    sleep(0.5)
    print(f'O maior valor informado foi {max(numeros)}.')
    print('-=' * 23)


maior(2, 9, 4, 5, 7, 1)
