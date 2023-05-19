'''
Desenvolva um programa que leia nome, idade e sexo
de 4 pessoas.

a média de idades do grupo
qual é o nome do homem mais velho
qntas mulheres tem menos de 20 anos

'''
soma_idade = int(0)
h_mais_velho = int(0)
nome_h_mais_velho = str('')
mulheres_novas = int(0)

for c in range(1,5):
    print('------ {}° PESSOA ------'.format(c))
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO (M/F): ')).strip().upper()

    soma_idade = idade+soma_idade

    if sexo == 'M':
        if idade > h_mais_velho:
            h_mais_velho = idade
            nome_h_mais_velho = nome

    if sexo == 'F':
        if idade <= 20:
            mulheres_novas = mulheres_novas +1

media_idade = soma_idade / 4

print('A média de idades é de {} anos'.format(media_idade))
print('O homem mais velho se chama {}, e ele tem {} anos'.format(nome_h_mais_velho,h_mais_velho))
print('Há um total de {} mulheres com até 20 anos na lista'.format(mulheres_novas))
