massa = float(input('Qual é a sua massa? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = massa / (altura ** 2)
print('Seu IMC é {:.1f} , tu tas '.format(imc),end='')
if imc < 18.5:
    print('abaixo do peso.')
elif 18.5 <= imc < 25:
    print('com peso ideal.')
elif 25 <= imc < 30:
    print('em sobrepeso.')
elif 30 <= imc < 40:
    print('em obesidade.')
elif imc > 40:
    print('em obesidade morbida.')