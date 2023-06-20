def metade(num, formate=False):
    return num / 2 if formate is False else moeda(num)


def dobro(num, formate=False):
    return num * 2 if formate is False else moeda(num)


def aumento_10(num, formate=False):
    return num + ((10/100) * num) if formate is False else moeda(num)


def moeda(num=0, moedas='€', formate=False):
    return f'{num:.2f}{moedas}'.replace('.', ',') if formate is False else moeda(num)


def resumo(num, formate=False):
    print('-' * 30)
    print('Resumo do valor')
    print('-' * 30)
    print(f'Preço analisado: {moeda(num)}')
    print(f'Dobro do preço: {moeda(dobro(num))}')
    print(f'Metade do preço: {moeda(metade(num))}')
    print(f'Aumento 10% do preço: {moeda(aumento_10(num))}')
    print('-' * 30)
    return num