casa = float(input('Valor da casa: $'))
sala = float(input('Salário do comprador: $'))
anos = int(input('Quantos anos de financiamento? '))
presta = (casa / 12) / anos
print('Para pagar uma casa de ${} em {} anos a prestação será ${:.2f}.'.format(casa,anos,presta))
if presta >= (30/100) * sala:
    print('Empréstimo negado.')
else:
    print('Emprestimo aprovado.')
