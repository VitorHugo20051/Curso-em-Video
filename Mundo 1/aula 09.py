frase = "Za Warudo"
print(frase[3]) # vai mostrar a quarta letra pois começa-se a contar a partir do 0
print(frase[3:9]) # vai mostrar o que está entre a terceira e nona posição ("Warudo")
print(frase[:2]) # vai mostrar a partir do inicio até á posição 3
print(frase[2:]) # vai mostrar a partir da posição 3 até ao fim
print(frase[0:9:2]) # vai mostrar o que está entre a posição 0 e 9 mas contando dois em dois
print(frase[3::3]) # começa a partir da posição 3 e mostra de 3 em 3 até ao final da string
print(len(frase)) # vai mostrar quantos caracteres tem a stirng
print(frase.count('a')) # vai mostrar quantas vezes aparece a letra 'a'
print(frase.count('a',0,4)) # vai mostrar quantas vezes aparece a letra 'a' entre as posições 0 e 4(sem contar com a posição 4)
print(frase.find('Za')) # vai mostrar onde começa 'Za'
print(frase.find('confia'))# vai mostrar -1 pois 'confia' não está na string
print('Warudo' in frase) # vai dizer se 'Warudo' está na string ( vai mostrar true or false)
print(frase.replace('Za Warudo','O Mundo')) # troca 'Za Warudo' por 'O Mundo'
print(frase.upper()) # mete tudo maisculo
print(frase.lower()) # mete tudo minusculo
print(frase.capitalize()) # mete só o primeiro caracter maisculo e o resto minusculo
print(frase.title()) # mete a primeira letra de cada palavra maiscula
fras = '   Za Warudo  '
print(fras.strip()) # remove os espaços do inicio e do fim
print(fras.rstrip()) # remove os espaços do fim
print(fras.lstrip()) # remove os espaços do inicio
print(frase.split()) # ocorre uma divisao na string e põe numa lista
print(' '.join(frase))