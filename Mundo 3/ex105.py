def notas(*nota, sit):
    alunos = list(nota)
    media = sum(alunos) / len(alunos)
    dicio = dict()
    dicio['total'] = len(alunos)
    dicio['maior'] = max(alunos)
    dicio['menor'] = min(alunos)
    dicio['média'] = media
    if sit is True:
        if media >= 7:
            dicio['situação'] = 'BOA'
        elif 5 <= media <= 6:
            dicio['situação'] = 'RAZOÁVEL'
        elif media < 5:
            dicio['situação'] = 'RUIM'
    return dicio


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
