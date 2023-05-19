# Faça um algoritmo que leia o salario de um funcionário
# e mostre o seu novo salário, com 15% de aumento.
s = float(input('Qual salário do funcionário? R$ '))
a = float(input('Qual a % de aumento? '))
ns = float(s+(s*a/100))
print("O novo salário será de: R$ {:.2f}".format(ns))
