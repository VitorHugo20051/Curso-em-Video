genero = str(input('Digite o seu género: [M/F] ')).upper().strip()
while genero not in 'FM':
    genero = str(input('Dados inválidos. Por favor, informe seu género: ')).upper().strip()
if genero == 'F':
    print('Género feminino registrado com sucesso.')
else:
    print('Género masculino registrado com sucesso.')
