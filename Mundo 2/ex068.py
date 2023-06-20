import random
print('Vamos jogar par ou ímpar!')
pc = random.randint(1,10)
cont = 0
while True:
    jogador = int(input('Digite um valor: '))
    par_impar = str(input('Par ou Ímpar: [P/I] ')).strip().upper()[0]
    soma = jogador + pc
    if soma % 2 == 0:
        print(f'Tu jogaste {jogador} e o pc {pc}.A soma foi {soma} que é par')
        if par_impar in 'P':
            print('Ganhaste!')
            cont += 1
        else:
            break
    elif soma % 2 != 0:
        print(f'Tu jogaste {jogador} e o pc {pc}.A soma foi {soma} que é impar.')
        if par_impar in 'I':
            print('Ganhaste!')
            cont += 1
        else:
            break

print('Perdeste!')
print(f'Game over! Você venceu {cont} vezes. ')



