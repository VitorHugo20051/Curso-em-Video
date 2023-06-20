num = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezasseis','dezessete', 'dezoito', 'dezenove', 'vinte')
n1 = int(input('Digite um número entre 0 e 20: '))
while n1 not in range(0,21):
    print('Número inválido! Tente novamente.')
    n1 = int(input('Digite um número entre 0 e 20: '))
print(f'Você digitou o número {num[n1]}.')
