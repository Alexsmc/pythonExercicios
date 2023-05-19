'''
Crie um programa que leia o ano de nascimento de 7 pessoas
e diga qntas são maiores de idade
'''

from datetime import date

atual = date.today().year
maior = int(0)
menor = int(0)
for c in range(1,8):
    pessoa = int(input('Qual ano de nastimento da pessoa {}: '.format(c)))
    if (atual - pessoa) >= 18:
        maior = maior +1
    else:
        menor = menor +1
print('{} pessoas são maiores de 18 anos.'.format(maior))
print('{} pessoas são menores de 18 anos.'.format(menor))