'''
crie um programa que calcula o aumento de um salário de um funcionário
para salários acime de R$ 1.200,00 o aumento será de 10%
para salarios abaixo disso o aumento será  de 15%
'''
salario = float(input('Qual o salário? R$'))
if salario >= 1200.00:
    novo_salario = salario * 0.1 + salario
else:
    novo_salario = salario * 0.15 + salario

print('Novo salário será de: R${:.2f}'.format(novo_salario))