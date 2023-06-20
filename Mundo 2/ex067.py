tabu = 0
while True:
    tabu = int(input('Quer ver a tabuada de que número? '))
    if tabu < 0:
        break
    for c in range(1, 11):
        print(f'{tabu} x {c} = {tabu * c}')

print('O programa encerrou! Volte sempre!')