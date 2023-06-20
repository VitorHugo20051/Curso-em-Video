def metade(num):
    return num / 2


def dobro(num):
    return num * 2


def aumento_10(num):
    return num + ((10/100) * num)


def moeda(num=0, moedas='€'):
    return f'{num:.2f}{moedas}'.replace('.', ',')