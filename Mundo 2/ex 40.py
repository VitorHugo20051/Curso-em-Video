m1 = float(input('Primeira nota: '))
m2 = float(input('Segunda nota: '))
media = (m1 + m2) / 2
print('Quem teve {:.1f} e {:.1f} tem uma média de {:.1f}.'.format(m1,m2,media))
if media < 9.5:
    print('Já foste!!')
elif 9.5 < media < 11.9:
    print('Recuperação!!')
elif media > 12:
    print('Aprovado!!')
