dados_pessoa = dict()
dados_total = list()
cont = 0
lista_mulheres = list()
lista_idade = list()
media = 0
lista_acima_media = list()

while True:
    dados_pessoa.clear()
    dados_pessoa["nome"] = str(input('Nome: '))
    while True:
        dados_pessoa["genero"] = str(input('Género[M/F]: ')).upper().strip()
        if dados_pessoa["genero"] in 'MF':
            break
        print('Erro, responda M ou F.')
    dados_pessoa["idade"] = int(input('Idade: '))
    dados_total.append(dados_pessoa.copy())
    if dados_pessoa['genero'] == 'F':
        lista_mulheres.append(dados_pessoa['nome'])
    if dados_pessoa['idade'] not in lista_idade:
        lista_idade.append(dados_pessoa['idade'])
        media = sum(lista_idade) / len(lista_idade)
    while True:
        escolha = str(input('Quer continuar? [S/N] ')).upper().strip()
        if escolha in 'SN':
            break
        elif escolha != 'S' and 'N':
            print('Erro.Por favor responda apena S ou N.')
    if escolha in 'N':
        break

print(f'Ao todo {len(dados_total)} pessoas foram cadastradas.')
print(f'A média da idade é de {media:.2f} anos.')
print(f'As mulheres cadastradas foram: ')
for c in lista_mulheres:
    print(f'{c}')

for p in dados_total:
    if p['idade'] > media:
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
