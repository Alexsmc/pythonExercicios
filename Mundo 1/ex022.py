print(''' Crie um programa que leia o nome completo de uma pessoa e mostra
 - O nome com todas as letras maiusculas
 - o nome com todas as letras minuscuas
 - Quantas letras ao todo sem considerar os espaços
 - Quantas letras tem o primeiro nome  ''')

nome = str(input('Qual seu nome?: ')).strip()
print('Analisando seu nome....')
print('Seu nome em maiusculo é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é: {} e tem {} letras.'.format(separa[0], len(separa[0])))
print(len(separa))
print(separa)