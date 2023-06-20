brasil = []
estado = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado)
brasil.append(estado2)

print(brasil[0]['sigla'])

distrito = {}
portugal = []

for c in range(0,3):
    distrito['distrito'] = str(input('Distrito: '))
    distrito['concelho'] = str(input('Concelho: '))
    portugal.append(distrito.copy())
for d in portugal:
    for k, v in d.items():
        print(f'O campo {k} tem o valor {v}.')