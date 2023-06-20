sala = float(input('Qual o seu salário? '))
if sala <= 1250.00:
    aumen = sala + (sala * (15/100))
    print('Com um aumento de 15% seu salário será de {:.2f} €.'.format(aumen))
if sala >= 1250:
    aumen = sala + (sala * (10/100))
    print('Com um aumento de 10% seu salário será de {:.2f} €.'.format(aumen))