print('''Faça um programa que leia o nome completo de uma pessoa
e mostre em seguida o primeiro e o ultimo nome separadamente

Ex:  Ana MAria de Souza
primeiro nome = Ana
Ultimo Nome = Souza''')

nome = str(input('Sigite sue nome: ')).strip()
separa = nome.split()
print('Primeiro nome: {}'.format(separa[0]))
print('Ultimo nome: {}'.format(separa[len(separa)-1]))
