'''
Faça um programa que leia 3 numeros e mostre qual o maior e qual o menor
'''

number_1 = int(input('Digite o numero 1: '))
number_2 = int(input('Digite o numero 1: '))
number_3 = int(input('Digite o numero 1: '))
maior = 0
menor = 0

if (number_1>number_2) and (number_1>number_3):
    maior = number_1
if (number_2>number_1) and (number_2>number_3):
    maior = number_2
if (number_3>number_1) and (number_3>number_2):
    maior = number_3
if (number_1<number_2) and (number_1<number_3):
    menor = number_1
if (number_2<number_1) and (number_2<number_3):
    menor = number_2
if (number_3<number_1) and (number_3<number_2):
    menor = number_3
print('O maior numero é: {}'.format(maior))
print('O menor numero é: {}'.format(menor))