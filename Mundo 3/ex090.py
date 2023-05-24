aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input('Média: '))
print(f'O aluno: {aluno["nome"]}')
print(f'Teve média: {aluno["média"]}')
if aluno['média'] < 7:
    print('Situação: REPROVADO')
else:
    print('Situação: APROVADO')
