cont = 0
expressao = str(input('Digite a expressão: ')).strip()

for c in expressao:
    if c == '(':
        cont += 1
    elif c == ')':
        cont -= 1
        if cont < 0:
            print('Expressão inválida.')
            exit(0)
if cont != 0:
    print('Expressão inválida.')
else:
    print('Expressão válida.')
