tupla = ('cachorro', 'gato', 'cobra', 'elefante', 'paralelepipedo')
for c in tupla:
    print(f'\nNa palavra {c} temos ', end='')
    for letra in c:
       if letra.lower() in 'aeiou':
           print(letra, end='')