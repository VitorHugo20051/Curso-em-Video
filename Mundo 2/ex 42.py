a = float(input('Primeiro lado: '))
b = float(input('Segundo lado: '))
c = float(input('Terceiro lado: '))
if a < b + c and b < a + c and c < a + b:
    if a == b and a == c and b == c:
        print('Estes lados formam um triangulo equilatero.')
    elif a != b and a == c or a == b and a != c or a != b and b == c:
        print('Estes lados formam um triangulo isosceles.')
    elif a != b and a != c and b != c:
        print('Estes lados formam um triangulo escaleno.')
else:
    print('Estes lados não formam um triangulo.')



