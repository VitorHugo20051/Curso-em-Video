import math
ang = float(input("Digite o angulo: "))
seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print("O seno do seu angulo é {:.2f}.".format(seno))
print("O cosseno do seu angulo é {:.2f}.".format(cos))
print("O tangente do seu angulo é {:.2f}.".format(tan))