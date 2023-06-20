print('LOJA DO CHINÊS')
mais_mil = 0
soma = 0
menor = cont = barato = 0
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: € '))
    cont += 1
    continua = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    soma += preço
    if preço > 1000:
        mais_mil += 1
    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    if continua in 'N':
        break
print(f'Total da compra: {soma:.2f}€')
print(f'Temos {mais_mil} produtos que custa mais de 1000€.')
print(f'O produto mais barato foi {barato} que custa {menor}€.')