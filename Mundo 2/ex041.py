'''
categoria de atleta de acordo com a idade
até 9 mirim
até 14 infantil
até 19 junior
até 20 senior
acima master
'''
from datetime import date
ano = int(input('Em que ano vc nasceu? '))
atual = date.today().year
idade = atual - ano

print('Você tem {} anos, sua categoria é:'.format(idade))
if idade <= 9:
    print('MIRIM')
elif 9 < idade <= 14:
    print('INFANTIL')
elif 14 < idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')

