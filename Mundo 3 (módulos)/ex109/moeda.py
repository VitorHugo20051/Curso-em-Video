def metade(num, formate=False):
    return num / 2 if formate is False else moeda(num)


def dobro(num, formate=False):
    return num * 2 if formate is False else moeda(num)


def aumento_10(num, formate=False):
    return num + ((10/100) * num) if formate is False else moeda(num)


def moeda(num=0, moedas='€', formate=False):
    return f'{num:.2f}{moedas}'.replace('.', ',') if formate is False else moeda(num)