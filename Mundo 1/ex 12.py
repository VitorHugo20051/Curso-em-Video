pro = float(input("Qual o preço do produto? €"))
desc = pro - (pro * 5/100)
print("O produto que custava {}€ com o desconto de 5% custará {:.2f}€.".format(pro,desc))