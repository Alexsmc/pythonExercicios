
# Faça um programa que leia algo pelo teclado e mostre na tela o
# seu tipo primitivo e todas as informações possiveis sobre ela

text = (input('Digita alguma coisa ai: '))
print('O tipo primitivo desse valor é:', type(text))
print('Só tem espaçoes? {}' .format(text.isspace()))
print('É um numero? {}' .format(text.isnumeric()))
print('É alfabetico? {}'.format(text.isalpha()))
print('É alfanumerico? {}' .format(text.isalnum()))
print('Está em maiusculas? {}'.format(text.isupper()))
print('Está em minusculo? {}'.format(text.islower()))
print('Está capitalizada? {}'.format(text.istitle()))
