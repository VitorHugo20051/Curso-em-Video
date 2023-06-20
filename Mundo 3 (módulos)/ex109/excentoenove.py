from ex109 import moeda

numero = float(input('Digite o preço: €'))
print(f'A metade de {moeda.moeda(numero)} {moeda.metade(numero)}.')
print(f'A dobro de {moeda.moeda(numero)} é {moeda.dobro(numero)} .')
print(f'Aumentando 10% temos, {moeda.aumento_10(numero)} .')