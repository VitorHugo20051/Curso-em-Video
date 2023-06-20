

def leiaint(a: str):
    while True:
        valor = input(a)
        if valor.isnumeric():
            return int(valor)
        else:
            print('Erro! Digite um número inteiro válido.')


n = leiaint('Digite um número: ')
print(f'O número digitado foi {n}.')