aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
print(f'O aluno: {aluno["nome"]}')
print(f'Teve média: {aluno["média"]}')
if aluno['média'] < 7:
    print('Situação: REPROVADO')
else:
    print('Situação: APROVADO')
