nome = str(input("Digite seu nome completo: ")).strip() # elemina espaços no final
print("Analisando seu nome...")
print("Seu nome em maiusculas é {}.".format(nome.upper()))
print("Seu nome em minusculas é {}.".format(nome.lower()))
print("Seu nome tem ao todo {} letras.".format(len(nome)-nome.count(" "))) # - count elemina espaços na frente
prima = nome.split() # põe os nomes numa lista
print("Seu primeiro nome é {} e ele tem {} letras.".format(prima[0],len(prima[0])))
