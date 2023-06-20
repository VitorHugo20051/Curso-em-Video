veloci = float(input('Qual e a velocidade atual do carro? '))
multa = (veloci - 80) * 7
if veloci <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('MULTADO! Voce foi multado em {:.2f} € por exceder o limite de velocidade de 80 km/h.'.format(multa))