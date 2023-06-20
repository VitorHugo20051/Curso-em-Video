masc = menor20 = mais18 = 0
while True:
    print('Cadraste uma pessoa')
    idade = int(input('Idade: '))
    genero = str(input('Genero: [M/F] ')).strip().upper()[0]
    continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if genero in 'M':
        masc += 1
    if genero in 'F' and idade < 20:
        menor20 += 1
    if idade > 18:
        mais18 += 1
    if continua in 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {mais18}')
print(f'Total de homens cadastrados: {masc}')
print(f'Total de mulheres com menos de 20 anos: {menor20}')