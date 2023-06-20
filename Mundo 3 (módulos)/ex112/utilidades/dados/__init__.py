def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '' or entrada.isalnum():
            print(f'ERRO!"{entrada}" é um preço inválido!')
            entrada = str(input(msg))
        else:
            valido = True
            return float(entrada)