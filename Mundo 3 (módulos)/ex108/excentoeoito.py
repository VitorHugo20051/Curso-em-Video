from ex108 import moeda

numero = float(input('Digite um número: €'))
print(f'A metade de {moeda.moeda(numero)} {moeda.moeda(moeda.metade(numero))}.')
print(f'A dobro de {moeda.moeda(numero)} é {moeda.moeda(moeda.dobro(numero))} .')
print(f'Aumentando 10% temos, {moeda.moeda(moeda.aumento_10(numero))} .')