dados = dict()
dados['nome'] = str(input('Nome: '))
dados['media'] = float(input(f'Média de {dados["nome"]}: '))
if dados['media'] < 5:
    dados['situaçao'] = 'Reprovado'

elif 5 <= dados['media'] < 7:
    dados['situaçao'] = 'Recuperação'

elif dados['media'] >= 7:
    dados['situaçao'] = 'Aprovado'

for k, v in dados.items():
    print(f'{k} é igual a {v}.')