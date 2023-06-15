aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
print(f'O aluno: {aluno["nome"]}')
print(f'Teve média: {aluno["média"]}')

def situar(media):
    if media < 7:
        return 'REPROVADO'
    elif 5 <= media < 7:
        return 'RECUPERAÇÃO'
    else:
        return 'REPROVADO'
    pass


aluno['situação'] = situar(aluno["média"])

def imprimir_aluno():
    for k, v in aluno.items():
        print(f'   - {k} é igual {v}')
imprimir_aluno()
