pessoas = {
    'nome': 'Vitor',
    'género': 'M',
    'idade': 17
}
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.items())
print(pessoas.keys())
print(pessoas.values())

for k in pessoas.keys():
    print(k)

for v in pessoas.values():
    print(v)

for i in pessoas.items():
    print(i)

del pessoas['género']
print(pessoas)