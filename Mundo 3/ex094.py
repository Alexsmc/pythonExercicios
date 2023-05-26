pessoas = []
dados = {}
idade = total_idade = 0
while True:
    dados['Nome'] = str(input('Nome: '))
    idade = int(input('Idade: '))
    dados['Idade'] = idade
    total_idade += idade
    dados['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
    while dados['Sexo'] not in 'FM':
        print('Informação errada')
        dados['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
    pessoas.append(dados.copy())
    opc = str(input('Quer continuar? [S/N]')).strip().upper()
    if opc in 'nN':
        break
print('-='*30)
print(f'- Foram cadastradas {len(pessoas)} pessoas.')
media_idade = total_idade / len(pessoas)
print(f'- A média de idade do grupo é de: {media_idade:.2f} anos.')
print('As mulheres cadastradas foram: ', end='')
for i in pessoas:
    if i['Sexo'] in 'fF':
        print(i["Nome"], end=' ')
print()
print('- Lista das pessoas que estão acima da média: ')
for i in pessoas:
    if i['Idade']>media_idade:
        print(i)