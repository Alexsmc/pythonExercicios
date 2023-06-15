Galera = []
Pessoa = {}
idade = total_idade = 0
while True:
    Pessoa['Nome'] = str(input('Nome: '))
    idade = int(input('Idade: '))
    Pessoa['Idade'] = idade
    total_idade += idade
    while True:
        Pessoa['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
        if Pessoa['Sexo'] in 'mMfF':
            break
        print('ERRO! digite apenas M ou F')
    Galera.append(Pessoa.copy())
    while True:
        opc = str(input('Quer continuar? [S/N]')).strip().upper()
        if opc in 'sSnN':
            break
        print('ERRO! Digite apenas S ou N')
    if opc in 'nN':
        break
print('-='*30)
print(f'- Foram cadastradas {len(Galera)} pessoas.')
media_idade = total_idade / len(Galera)
print(f'- A média de idade do grupo é de: {media_idade:5.2f} anos.')
print('As mulheres cadastradas foram: ', end='')
for i in Galera:
    if i['Sexo'] in 'fF':
        print(i["Nome"], end=' ')
print()
print('- Lista das pessoas que estão acima da média: ')
for i in Galera:
    if i['Idade'] >= media_idade:
        print('  ')
        for k, v in i.items():
            print(f'{k} = {v}; ', end=' ')
        print()
print('<< ENCERRADO >>')
