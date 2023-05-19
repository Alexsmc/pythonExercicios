'''
Escreva um programa pra aprovar um emprestimo bancário
para a compra de uma casa. O programa vai perguntas o valor da casa,
o salário do comprador e em qnatos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do
salário ou então o emprestimo será negado.
'''

print('=-'*20)
print('BEM VINDO AO BANCO!')
print('=-'*20)
menu = int(1)
while menu == 1:
    vcasa = float(input('Qual o valor da casa desejada? R$ '))
    salario = float(input('Qual o seu salário? R$'))
    anos = int(input('Em quantos anos vc pagará? '))
    meses = anos * 12
    prestacao = vcasa / meses

    if prestacao < (salario * 30/100):
        print('PAREBÉNS SEU FINANCIAMENTO FOI APROVADO')
        print('O valor da prestação ficou em: {}x de R$ {:.2f}'.format(meses, prestacao))
        menu = int(input('\nDigite 1 para uma nova consulta ou 0 para sair.'))
    else:
        print('Infelizmente seu financiamento não foi aprovado! Tente outra vez')
        menu = int(input('\nDigite 1 para uma nova consulta ou 0 para sair.'))
print('OBRIGADO PELA SUA VISITA!')