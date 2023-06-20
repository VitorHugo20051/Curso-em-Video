continua = 'S'
soma = count = media = maior = menor = 0
while continua != 'N':
    num = int(input('Digite um número: '))
    soma += num
    count += 1
    if count == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    continua = str(input('Queres continuar? [S/N] ')).strip().upper()
media = soma / count
print(f'Você digitou {count} números e a média foi {media:.2f}.')
print(f'O maior valor foi {maior} e menor foi {menor}.')