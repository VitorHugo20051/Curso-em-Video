num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()
num.insert(3, 2)
num.pop() # pop.() apaga o ultimo elemento
num.remove(2) # quando tem há varios elementos iguais, vai ser apagado o primeiro
if 4 in num:
    num.remove(4)
else:
    print('Não encontrei o 4.')
print(num)
print(f'Esta lista tem {len(num)} elementos.')



valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for valor in enumerate(valores):  # enumerate diz a posição do valor
    print(f'{valor}...',end='')