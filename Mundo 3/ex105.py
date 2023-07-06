def notas(*n, sit=False):
    '''
    -> Fução pega todas as notas de uma turma e devolve a média, maior e menor nota asism como
    a situação da turma.
    :param n: uma ou mais notas dos alunos
    :param sit:  valor opcional indicando se deve ou não adicionar
    :return: as infroamção e a situação da turma
    '''

    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


# Main
resp = notas(5.4, 8.6, 10.0, 9.4, 0.5, sit=True)
print(resp)
