bunito = '-' * 5
nome_velho = ''
soma_idade = 0
mais_velho = 0
soma_idade = 0
total_mulher20 = 0
for p in range(1, 5):
    print('{}{}ª PESSOA{}'.format(bunito, p, bunito))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    genero = str(input('Género [M/F]: ')).upper().strip()
    soma_idade += idade
    if p == 1 and genero == 'M':
        mais_velho = idade
        nome_velho = nome
    if genero == 'M' and idade > mais_velho:
        mais_velho = idade
        nome_velho = nome
    if genero == 'F' and idade < 20:
        total_mulher20 += 1
media_idade = soma_idade / 4
print('A média de idade no grupo é de {:.1f} anos.'.format(media_idade))
print('O homem mais velho é o {} e tem {} anos.'.format(nome_velho, mais_velho))
print('O número de mulheres menor de 20 anos é {}.'.format(total_mulher20))