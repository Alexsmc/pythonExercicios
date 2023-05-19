'''
O memso professor do desafio anterior que escolher a ordem de apresentação dos alunos
'''

from random import shuffle
a = input('Aluno 1: ')
b = input('Aluno 2: ')
c = input('Aluno 3: ')
d = input('Aluno 4: ')
o = [a, b, c, d]
shuffle(o)
print('Os alunos sorteados serão:\n{}'.format(o))
