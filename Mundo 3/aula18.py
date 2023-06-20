teste = list()
teste.append('Vitor')
teste.append(17)
galera = list()
galera.append(teste[:]) # '[:] faz uma cópia dos dados da lista
teste[0] = 'João'
teste[1] = 18
galera.append(teste[:])
print(galera)