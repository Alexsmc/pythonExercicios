# Desafio 7
#Desenvolva um programa que leia as notas
#de um aluno e calcula a média.

n1 = float(input('Nota do teste: '))
n2 = float(input('Nota da prova: '))
m = float((n1+n2) / 2)
print('Nota do teste: {}\nNota da prova: {}'.format(n1, n2))
print('Média: {:.1f}'.format(m))
