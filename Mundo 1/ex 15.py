dia = int(input("Quantos dias alugado? "))
km = float(input("Quantos km rodados? "))
total = (dia * 60) + (km * 0.15)
print("O total a pagar é de {:.2f}€.".format(total))