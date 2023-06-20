def area():
    print('Controlo de terreno')
    larg = float(input('Largura (m): '))
    comp = float(input('Comprimento (m): '))
    área = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {área:.1f}m2.')


area()