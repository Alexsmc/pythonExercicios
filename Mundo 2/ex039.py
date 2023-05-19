'''
Crie um programa que leia o ano de nascimento do usuário
 que diga qunado ele vai se alistar, se já é hora de se alistar
 e qnto tempo ele passou de se alistar.
'''
from datetime import date
ano = int(input('Qual o seu ano de nascimento: '))
atual = date.today().year
idade = atual - ano

if idade < 18:
    print('Ainda falta {} anos para você se alistar!'.format(18-idade))
elif idade > 18:
    print('Já passou o tempo de se alistar. vc está {} anos atrasado.'.format(idade-18))
else:
    print('ALISTAMENTO MILITAR!! CHEGOU A HORA!!')
