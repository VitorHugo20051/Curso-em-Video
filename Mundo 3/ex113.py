def leiaint(a):
    while True:
        try:
            num = int(input(a))
        except (ValueError, TypeError):
            print('Erro, por favor digite um número inteiro válido.')
            continue
        except KeyboardInterrupt:
            print('O usuário decidiu não digitar os dados.')
            print('Volte sempre!')
            break
        else:
            return num


def leiafloat(b):
    while True:
        try:
            number = float(input(b))
        except (ValueError, TypeError):
            print('Erro, por favor digite um número real válido.')
            continue
        except KeyboardInterrupt:
            print('O usuário decidiu não digitar os dados.')
            print('Volte sempre!')
            break
        else:
            return number


n = leiaint('Digite um número inteiro: ')
f = leiafloat('Digite um número real: ')
print(f'O número digitado inteiro foi {n} e real foi {f}.')