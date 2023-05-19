'''
Desenvolva um progrma que pergunte a distanvia de uma viagem em km.
Calcule o preço da passagem cobrando R$ 0,50 por km para viagens de até 200km
e RS 0,45 para viagens mais longas.
'''

viagem = int(input('Qual distancia de sua viagem? '))
if viagem <= 200:
    print('Valor da viagem é: RS{:.2f}'.format(viagem*0.5))
else:
    print('Valor da viagem é R${:.2f}'.format(viagem*0.45))
