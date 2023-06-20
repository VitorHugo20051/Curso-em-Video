from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Sedundo valor: '))
opçao = 0
while opçao != 5:
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')
    opçao = int(input('Qual é a sua opção? '))
    if opçao == 1:
        print('A soma entre {} e {} é {}.'.format(n1, n2, n1 + n2))
    elif opçao == 2:
        print('O produto entre {} e {} é {}.'.format(n1, n2, n1 * n2))
    elif opçao == 3:
        if n1 > n2:
            print('O número {} é maior que {}.'.format(n1, n2))
        if n1 < n2:
            print('O número {} é maior que {}.'.format(n2, n1))
        else:
            print('Os números são iguais.')
    elif opçao == 4:
        print('Informe os novos números.')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Sedundo valor: '))
    elif opçao == 5:
        sleep(1)
        print('Finalizando...')
    else:
        print('Opção inválida.')
print('Fim do programa!')