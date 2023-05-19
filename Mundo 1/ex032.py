'''
Faça um programa que lê um ano qualquer e diga se é um ano bissexto
'''
from datetime import date
ano = int(input('Digite o ano: Coloque 0 par ao ano atual '))
if ano == 0:
    ano = date.today().year
if (ano % 4)==0 and (ano % 100)!=0 or (ano % 400) == 0:
    print('O ano {} é um ano bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))