'''
Um professor que sortear um dos seus quarto alunos para apagar o quadro.
faça um progrma que ajude ele, lendo o nome deles e escrevendo o nome escolhido
'''
from random import choice

a = input('Aluno 1: ')
b = input('Aluno 2: ')
c = input('Aluno 3: ')
d = input('Aluno 4: ')

print('O alunos escolhido foi: {}'.format(choice([a,b,c,d])))
