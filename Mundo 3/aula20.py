def soma(a, b):
    print(f'A = {a} e B = {b}.')
    s = a + b
    print(f'A soma de A + B = {s}.')


soma(2, 3)
soma(b=5, a=8)


def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} que são ao todo {tam} números.')


contador(1, 2, 3)


def dobro(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [2, 3, 4, 5, 0]
dobro(valores)
print(valores)