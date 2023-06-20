dista = float(input('Qual a distancia da sua viagem? '))
preçoM = dista * 0.45
precom = dista * 0.50
print('Voce irá iniciar uma viagem de {} km.'.format(dista))
if dista <= 200:
    print('A sua viagem custará {:.2f} €. Boa viagem!!'.format(precom))
else:
    print('A sua viagem custará {:.2f} €. Boa viagem!!'.format(preçoM))