l = float(input("largura da parede: "))
a = float(input("altura da parede: "))
area = l * a
tinta = area / 2
print("As dimensões da sua parede são {}x{:.2f} e a sua area é {}m2.\nPara pintar essa parede é necessário {:.2f} litros de tinta.".format(l,a,area,tinta))
