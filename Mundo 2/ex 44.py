confia = 12 * '='
print('{} LOJA DO VITOR {}'.format(confia, confia))
price = float(input('Preço das compras: €'))
print('Formas de pagamento')
print('[ 1 ] á vista dinheiro/cheque')
print('[ 2 ] á vista no cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual é a sua opção? '))
if opcao == 1:
    preco = price - (price * (10/100))
    print('O preço final fica {:.2f} €.'.format(preco))
elif opcao == 2:
    preco = price - (price * (5/100))
    print('O preço final fica {:.2f} €.'.format(preco))
elif opcao == 3:
    print('O preço final é {:.2f} €.'.format(price))
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    parce = (price / parcelas)
    juros = parce + (parce * (20/100))
    preco = price + (price * (20/100))
    print('Sua compra com foi parcelada em {}x de {:.2f} € com juros,\nsua compra de {:.2f} € fica {:.2f} €.'.format(parcelas, juros, price, preco))