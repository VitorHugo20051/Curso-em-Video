frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inver = ''
for c in range(len(junto)-1, -1, -1):
    inver += junto[c]
print('A palavra {} ao contrario é {}.'.format(junto, inver))
if inver == junto:
    print('E um palindromo.')
else:
    print('Nao é um palindromo.')