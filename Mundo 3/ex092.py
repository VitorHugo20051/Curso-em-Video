from datetime import datetime
dados = dict()
ano_atual = datetime.today().year

dados['nome'] = str(input('Nome: '))
ano_nasc = int(input('Ano de Nascimento: '))
dados['carteira'] = int(input('Carteira de trabalho (0 não tem): '))
dados['idade'] = ano_atual - ano_nasc

if dados['carteira'] != 0:
    dados['ano_contra'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salário: $ '))
    dados['aposentadoria'] = dados['idade'] + 35
for k, v in dados.items():
    print(f'- {k} tem valor {v}')