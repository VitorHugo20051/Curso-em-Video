a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b   # a + b é diferente de b + a
d = b + a
print(c)
print(d)
print(len(c))
print(c.count(2))   # mostra quantas vezes o número 2 repete
print(c.index(8))   # mostra a posição do número 8

pessoa = ('vitor', 17, 'M', 62.12)
print(pessoa)
del pessoa  # apaga a tupla toda
print(pessoa)