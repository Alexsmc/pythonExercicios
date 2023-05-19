'''
Crie um programa que leia um numero inteiro e mostre
na tela se ele é par ou impar
Mudanças para teste
'''

numero = int(input('Digite o numero: '))
if (numero % 2) == 1:
    print('{} é Ímpar.'.format(numero))
else:
    print('{} é Par.'.format(numero))