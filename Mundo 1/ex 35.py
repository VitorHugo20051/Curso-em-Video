a = float(input('Primeiro lado: '))
b = float(input('Segundo lado: '))
c = float(input('Terceiro lado: '))
if a < b + c and b < a + c and c < a + b:
    print('Estes lados formam um triangulo.')
else:
    print('Estes lados não formam um triângulo.')